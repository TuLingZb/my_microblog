from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError,Length

from app.models import User
from flask_babel import lazy_gettext as _l




class EditProfileForm(FlaskForm):  # 在编辑配置文件表单中验证用户名。
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_l('Please use a different username.'))




class PostForm(FlaskForm):  # 博客文章内容编辑
    post = TextAreaField(_l('Say something'), validators=[
        DataRequired(), Length(min=1, max=140)
    ])
    submit = SubmitField(_l('Submit'))


from flask import request

class SearchForm(FlaskForm):
    q = StringField(_l('SearchForm'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)