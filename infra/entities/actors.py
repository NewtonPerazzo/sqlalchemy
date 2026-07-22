from infra.configs.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class Actors(Base):
    __tablename__ = "actors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    # pure relation between an element from a table and other
    movie_title: Mapped[str] = mapped_column(ForeignKey("movies.title"))

    # format print movie
    def __repr__(self) -> str:
        return f"Actor: name={self.name} - movie={self.movie_title}"