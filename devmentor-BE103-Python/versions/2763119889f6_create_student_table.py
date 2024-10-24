"""create student table

Revision ID: 2763119889f6
Revises: ff3c26ae043a
Create Date: 2024-10-24 14:05:09.337728

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2763119889f6'
down_revision: Union[str, None] = 'ff3c26ae043a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'students',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(255), nullable=False, index=True),
        sa.Column('age', sa.Integer(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('students')
