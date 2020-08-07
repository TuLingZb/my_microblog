from datetime import datetime
from hashlib import md5

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login
from time import time
import jwt
from flask import current_app

followers = db.Table(
    'followers',
    db.Column('followed_id', db.Integer, db.ForeignKey('user_info.id')),
    db.Column('follower_id', db.Integer, db.ForeignKey('user_info.id'))
)


from app.search import add_to_index, remove_from_index, query_index

class SearchableMixin(object):
    @classmethod
    def search(cls, expression, page, per_page):
        ids, total = query_index(cls.__tablename__, expression, page, per_page)
        if total == 0:
            return cls.query.filter_by(id=0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        print(ids,when)
        print('********',cls.id.in_(ids))
        return cls.query.filter(cls.id.in_(ids)).order_by(
            db.case(when, value=cls.id)), total

    @classmethod
    def before_commit(cls, session):
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }

    @classmethod
    def after_commit(cls, session):
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes = None

    @classmethod
    def reindex(cls):
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)

db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    followed = db.relationship(
        # User 表示关系当中的右侧实体（将左侧实体看成是上级类）
        # 由于这是自引用关系，所以两侧都是同一个实体。
        'User',

        # secondary 指定了用于该关系的关联表
        # 就是使用我在上面定义的 followers
        secondary=followers,

        # primaryjoin 指明了右侧对象关联到左侧实体（关注者）的条件
        # 也就是根据左侧实体查找出对应的右侧对象
        # 执行 user.followed 时候就是这样的查找
        primaryjoin=(followers.c.follower_id == id),

        # secondaryjoin 指明了左侧对象关联到右侧实体（被关注者）的条件
        # 也就是根据右侧实体找出左侧对象
        # 执行 user.followers 时候就是这样的查找
        secondaryjoin=(followers.c.followed_id == id),

        # backref 定义了右侧实体如何访问该关系
        # 也就是根据右侧实体查找对应的左侧对象
        # 在左侧，关系被命名为 followed
        # 在右侧使用 followers 来表示所有左侧用户的列表，即粉丝列表
        backref=db.backref('followers', lazy='dynamic'),
        lazy='dynamic'
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)

    __tablename__ = "user_info"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)
        # return 'https://www.gravatar.com/avatar/{}?s={}'.format(digest, size)

    def follow(self, user):  # 添加关注
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):  # 取消关注
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):  # 是否关注
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):  # Post联合查询
        followed = Post.query.join(    #关注用户的帖子
            followers, (followers.c.followed_id == Post.user_id)
        ).filter(
            followers.c.follower_id == self.id
        )
        own = Post.query.filter_by(user_id=self.id)  #自己发布的帖子
        # print(followed.union(own).order_by(Post.timestamp.desc()).all())
        return followed.union(own).order_by(Post.timestamp.desc())   #结果合并

    def get_reset_password_token(self,expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


class Post(SearchableMixin,db.Model):

    __searchable__ = ['body']

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    language = db.Column(db.String(5))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

    __tablename__ = "post_form"




@login.user_loader  # 加载用户id
def load_user(id):
    return User.query.get(int(id))


