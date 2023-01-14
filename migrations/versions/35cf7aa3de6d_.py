"""empty message

Revision ID: 35cf7aa3de6d
Revises: 2f6d35cd4b59
Create Date: 2023-01-11 11:02:09.990214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35cf7aa3de6d'
down_revision = '2f6d35cd4b59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('confirmed', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('confirmed')

    # ### end Alembic commands ###
