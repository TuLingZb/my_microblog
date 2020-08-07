from app import  db, moment,create_app
from app.models import User, Post

app = create_app()
# 设置
@app.shell_context_processor
def make_shell_content():
    return {'db': db, 'User': User, 'Post': Post,'moment':moment}