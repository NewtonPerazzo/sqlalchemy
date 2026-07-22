from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import Session

# configurations
engine = create_engine('mysql+pymysql://root:Root*0701@localhost:3306/cinema')
conn = engine.connect()
session = Session(engine)
# conn.execute(text('insert into movies (title, gender, year_movie) value ("avengers", "adventure", 2013)'))

# Entities
class Base(DeclarativeBase):
    pass
class Movies(Base):
    __tablename__ = "movies"

    title: Mapped[str] = mapped_column(primary_key=True)
    gender: Mapped[str] = mapped_column(nullable=False)
    year_movie: Mapped[int] = mapped_column(nullable=False)

    # format print movie
    def __repr__(self) -> str:
        
        return f"Movie (title={self.title} - year={self.year_movie} - gender={self.gender})"

# SQL

# INSERT
data_insert = Movies(
    title='Obssession', 
    year_movie=2026, 
    gender='horror'
)
# session.add(data_insert)
# session.commit()

# DELETE
# session.query(Movies).filter(Movies.title == 'avengers').delete()
# session.commit()

# UPDATE
session.query(Movies).filter(Movies.title == 'Obssession').update({ "year_movie": 2026, "gender": "horror" })
session.commit()

#  SELECT
data = session.query(Movies).all()

print(data)

session.close()