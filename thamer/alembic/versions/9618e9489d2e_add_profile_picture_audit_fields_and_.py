"""Add profile picture, audit fields, and login tracking to User model

Revision ID: 9618e9489d2e
Revises: ab52c3782a83
Create Date: 2025-01-06 19:55:22.518429

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = '9618e9489d2e'
down_revision: Union[str, None] = 'ab52c3782a83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'user',
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=func.now())
    )
    op.add_column(
        'user',
        sa.Column('profile_picture', sqlmodel.sql.sqltypes.AutoString(), nullable=True)
    )
    op.add_column(
        'user',
        sa.Column('last_login', sa.DateTime(), nullable=True)
    )
    op.add_column(
        'user',
        sa.Column('last_login_ip', sqlmodel.sql.sqltypes.AutoString(), nullable=True)
    )

    # Remove the server default for `updated_at` after migration
    op.alter_column('user', 'updated_at', server_default=None)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_login_ip')
    op.drop_column('user', 'last_login')
    op.drop_column('user', 'profile_picture')
    op.drop_column('user', 'updated_at')
    # ### end Alembic commands ###
