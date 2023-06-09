"""create posts table

Revision ID: 31e43cff5eb9
Revises: 
Create Date: 2023-03-21 17:01:22.343509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31e43cff5eb9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    
    op.drop_table('posts')
    pass
