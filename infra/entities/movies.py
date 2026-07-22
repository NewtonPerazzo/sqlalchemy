from infra.configs.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

class Movies(Base):
    __tablename__ = "movies"

    title: Mapped[str] = mapped_column(primary_key=True)
    gender: Mapped[str] = mapped_column(nullable=False)
    year_movie: Mapped[int] = mapped_column(nullable=False)
    actors = relationship("Actors", backref="actors", lazy="subquery")

    # format print movie
    def __repr__(self) -> str:
        return f"Movie - actors={self.actors} - title={self.title} - year={self.year_movie} - gender={self.gender})"