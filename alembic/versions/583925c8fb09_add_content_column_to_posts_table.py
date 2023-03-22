"""add content column to posts table

Revision ID: 583925c8fb09
Revises: 6773009b46e3
Create Date: 2023-03-21 19:22:30.945889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '583925c8fb09'
down_revision = '6773009b46e3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
