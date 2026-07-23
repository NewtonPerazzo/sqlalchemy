"""first

Revision ID: 698a5817e467
Revises: 
Create Date: 2026-07-23 08:12:18.147463

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '698a5817e467'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# alembic revision -m "{migration name - ex.: first}"

# alembic upgrade head
def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

# alembic downgrade -1
def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('account')
