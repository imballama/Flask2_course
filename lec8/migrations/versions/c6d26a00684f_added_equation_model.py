"""added equation model

Revision ID: c6d26a00684f
Revises: 28eb62ef8b10
Create Date: 2020-04-07 11:58:17.238101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6d26a00684f'
down_revision = '28eb62ef8b10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('a', sa.Integer(), nullable=True),
    sa.Column('b', sa.Integer(), nullable=True),
    sa.Column('c', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equation')
    # ### end Alembic commands ###
