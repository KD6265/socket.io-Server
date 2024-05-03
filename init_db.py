from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:Kd1606@localhost:7000/demodb")
if not database_exists(engine.url):
    create_database(engine.url)
    print('database created')
else:
    print('database already exists')

print("database exists:", database_exists(engine.url))

Base = declarative_base()

class demotb(Base):
    __tablename__ = 'demotb'

    id = Column(Integer, primary_key=True)
    top = Column(Integer)
    bottom = Column(Integer)
    left = Column(Integer)
    right = Column(Integer)
    
Base.metadata.create_all(engine)

# Step 5: Insert data into the database
Session = sessionmaker(bind=engine,autocommit=False, autoflush=False,)


print("Tables created successfully")