"""empty message

Revision ID: 013fdb122562
Revises: f9fee6dd928b
Create Date: 2021-08-10 12:57:14.136246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '013fdb122562'
down_revision = 'f9fee6dd928b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('experience', sa.Column('city', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('experience', 'city')
    # ### end Alembic commands ###
