"""添加language字段到数据库

Revision ID: 7a28286c0b60
Revises: d1b1197d19d5
Create Date: 2020-05-31 20:23:28.724535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a28286c0b60'
down_revision = 'd1b1197d19d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post_form', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post_form', 'language')
    # ### end Alembic commands ###
