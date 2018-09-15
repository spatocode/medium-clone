"""users table

Revision ID: 829e904977e4
Revises: 2dc694145013
Create Date: 2018-09-15 20:00:49.046349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '829e904977e4'
down_revision = '2dc694145013'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about', sa.String(length=200), nullable=True))
    op.create_index(op.f('ix_user_about'), 'user', ['about'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_about'), table_name='user')
    op.drop_column('user', 'about')
    # ### end Alembic commands ###