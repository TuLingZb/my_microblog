from flask import Blueprint

bp = Blueprint('errors',__name__)

from app.errors import handlers

# if __name__ == '__main__':
# print(__name__)