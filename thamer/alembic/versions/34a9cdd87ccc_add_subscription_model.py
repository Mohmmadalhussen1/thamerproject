"""Add subscription model

Revision ID: 34a9cdd87ccc
Revises: 1a8629c1ee47
Create Date: 2024-12-22 11:48:22.430820

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '34a9cdd87ccc'
down_revision: Union[str, None] = '1a8629c1ee47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
