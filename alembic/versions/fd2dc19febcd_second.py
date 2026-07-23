"""second

Revision ID: fd2dc19febcd
Revises: 698a5817e467
Create Date: 2026-07-23 09:36:29.797959

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from infra.repository.movies import MoviesRepository
from infra.entities.movies import Movies
from infra.entities.actors import Actors
from infra.configs.connection import DBConncetionHandler

# revision identifiers, used by Alembic.
revision: str = 'fd2dc19febcd'
down_revision: Union[str, Sequence[str], None] = '698a5817e467'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    movies_repository = MoviesRepository(DBConncetionHandler)
    movies_repository.insert(Movies(title='SpongeBob', gender='cartoon', year_movie=2010))


def downgrade() -> None:
    """Downgrade schema."""
    movies_repository = MoviesRepository(DBConncetionHandler)
    movies_repository.delete('SpongeBob')
