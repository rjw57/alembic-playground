"""Add a column

Revision ID: 3d358126a3f7
Revises: af5f57205c10
Create Date: 2022-03-26 16:23:05.699474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d358126a3f7'
down_revision = 'af5f57205c10'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade():
    op.drop_column('account', 'last_transaction_date')
