from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root:SecureWebHost@localhost/insite",echo = True)

from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Table, MetaData

meta = MetaData()

Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()



class sectors(Base):

    __tablename__ = 'sectors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sector = Column(Text)


class stocks(Base):

    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    stock = Column(Text)
    symbol = Column(String(255))
    sector_id = Column(Integer, ForeignKey('sectors.id', ondelete='CASCADE'))


class yearlyIncome(Base):

    __tablename__ = 'yearly_income'

    id = Column(Integer, primary_key=True, autoincrement=True)
    stocks_id = Column(Integer, ForeignKey('stocks.id', ondelete='CASCADE'))
    particulars = Column(Text)
    y5 = Column(Text, nullable=True)
    y4 = Column(Text, nullable=True)
    y3 = Column(Text, nullable=True)
    y2 = Column(Text, nullable=True)
    y1 = Column(Text, nullable=True)


class quarterlyIncome(Base):

    __tablename__ = 'quarterly_income'

    id = Column(Integer, primary_key=True, autoincrement=True)
    stocks_id = Column(Integer, ForeignKey('stocks.id', ondelete='CASCADE'))
    particulars = Column(Text)
    q6 = Column(Text, nullable=True)
    q5 = Column(Text, nullable=True)
    q4 = Column(Text, nullable=True)
    q3 = Column(Text, nullable=True)
    q2 = Column(Text, nullable=True)
    q1 = Column(Text, nullable=True)


class balanceSheet(Base):

    __tablename__ = 'balance_sheet'

    id = Column(Integer, primary_key=True, autoincrement=True)
    stocks_id = Column(Integer, ForeignKey('stocks.id', ondelete='CASCADE'))
    particulars = Column(Text)
    y4 = Column(Text, nullable=True)
    y3 = Column(Text, nullable=True)
    y2 = Column(Text, nullable=True)
    y1 = Column(Text, nullable=True)


class yearlyCashflow(Base):

    __tablename__ = 'yearly_cashflow'

    id = Column(Integer, primary_key=True, autoincrement=True)
    stocks_id = Column(Integer, ForeignKey('stocks.id', ondelete='CASCADE'))
    particulars = Column(Text)
    y4 = Column(Text, nullable=True)
    y3 = Column(Text, nullable=True)
    y2 = Column(Text, nullable=True)
    y1 = Column(Text, nullable=True)



