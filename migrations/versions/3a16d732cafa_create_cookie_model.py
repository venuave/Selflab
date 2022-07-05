"""create cookie model

Revision ID: 3a16d732cafa
Revises: 4a6f6d2af6e4
Create Date: 2022-07-05 16:37:18.785061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a16d732cafa'
down_revision = '4a6f6d2af6e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cookie_order',
    sa.Column('cookie_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('number_of_cookies', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cookie_id'], ['cookie.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('cookie_id', 'order_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cookie_order')
    # ### end Alembic commands ###
