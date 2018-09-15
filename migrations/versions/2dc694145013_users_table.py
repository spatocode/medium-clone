"""users table

Revision ID: 2dc694145013
Revises: 9b522025abbe
Create Date: 2018-09-15 19:35:09.666039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dc694145013'
down_revision = '9b522025abbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('birthdate', sa.Date(), nullable=True))
    op.add_column('user', sa.Column('photo', sa.BLOB(), nullable=True))
    op.create_index(op.f('ix_user_birthdate'), 'user', ['birthdate'], unique=True)
    op.create_index(op.f('ix_user_photo'), 'user', ['photo'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_photo'), table_name='user')
    op.drop_index(op.f('ix_user_birthdate'), table_name='user')
    op.drop_column('user', 'photo')
    op.drop_column('user', 'birthdate')
    # ### end Alembic commands ###