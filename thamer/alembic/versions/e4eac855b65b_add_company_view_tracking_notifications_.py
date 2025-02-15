"""Add company view tracking, notifications, and status updates

Revision ID: e4eac855b65b
Revises: 7f9159875586
Create Date: 2025-01-31 14:30:28.280528

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4eac855b65b'
down_revision: Union[str, None] = '7f9159875586'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company_views',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('viewer_id', sa.Integer(), nullable=True),
    sa.Column('viewed_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.ForeignKeyConstraint(['viewer_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_company_views_company_id', 'company_views', ['company_id'], unique=False)
    op.create_index('idx_company_views_viewed_at', 'company_views', ['viewed_at'], unique=False)
    op.create_index('idx_company_views_viewer_id', 'company_views', ['viewer_id'], unique=False)
    op.create_index(op.f('ix_company_views_company_id'), 'company_views', ['company_id'], unique=False)
    op.create_index(op.f('ix_company_views_viewer_id'), 'company_views', ['viewer_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_company_views_viewer_id'), table_name='company_views')
    op.drop_index(op.f('ix_company_views_company_id'), table_name='company_views')
    op.drop_index('idx_company_views_viewer_id', table_name='company_views')
    op.drop_index('idx_company_views_viewed_at', table_name='company_views')
    op.drop_index('idx_company_views_company_id', table_name='company_views')
    op.drop_table('company_views')
    # ### end Alembic commands ###
