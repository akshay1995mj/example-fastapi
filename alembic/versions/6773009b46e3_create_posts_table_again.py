"""create posts table again

Revision ID: 6773009b46e3
Revises: 31e43cff5eb9
Create Date: 2023-03-21 17:43:15.697447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6773009b46e3'
down_revision = '31e43cff5eb9'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:

    op.drop_table('posts')

    pass


