"""create cookie model

Revision ID: 59f58c5877be
Revises: 
Create Date: 2022-06-21 17:50:04.542725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59f58c5877be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cookie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=80), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cookie')
    # ### end Alembic commands ###
