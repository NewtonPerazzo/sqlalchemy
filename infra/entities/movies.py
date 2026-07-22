from infra.configs.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Movies(Base):
    __tablename__ = "movies"

    title: Mapped[str] = mapped_column(primary_key=True)
    gender: Mapped[str] = mapped_column(nullable=False)
    year_movie: Mapped[int] = mapped_column(nullable=False)

    # format print movie
    def __repr__(self) -> str:
        return f"Movie (title={self.title} - year={self.year_movie} - gender={self.gender})"