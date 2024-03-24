
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
engine = create_engine("mysql://root:SecureWebHost@localhost/insite",echo = True)

