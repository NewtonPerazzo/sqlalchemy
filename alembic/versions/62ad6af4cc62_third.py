"""third

Revision ID: 62ad6af4cc62
Revises: fd2dc19febcd
Create Date: 2026-07-23 09:47:26.827722

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from infra.repository.movies import MoviesRepository
from infra.entities.movies import Movies
from infra.entities.actors import Actors
from infra.configs.connection import DBConncetionHandler

# revision identifiers, used by Alembic.
revision: str = '62ad6af4cc62'
down_revision: Union[str, Sequence[str], None] = 'fd2dc19febcd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute(
        sa.text(
            """
            INSERT INTO movies (title, gender, year_movie)
            VALUES (:title, :gender, :year_movie)
            """
        ).bindparams(
            title="Im still here",
            gender="drama",
            year_movie=2025,
        )
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.execute(
        sa.text(
            """
            DELETE FROM movies
            WHERE title = :title
            """
        ).bindparams(title="Im still here")
    )