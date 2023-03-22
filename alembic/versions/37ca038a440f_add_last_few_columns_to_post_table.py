"""add last few columns to post table

Revision ID: 37ca038a440f
Revises: aa1388286155
Create Date: 2023-03-21 19:50:42.711180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37ca038a440f'
down_revision = 'aa1388286155'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', 
                  sa.Column('published', sa.Boolean(), 
                            nullable=False, server_default='TRUE'),)
    op.add_column('posts', 
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, 
                            server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
