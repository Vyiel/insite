import time

import schema
from schema import *
import pandas as pd
import logging

logging.disable(logging.INFO)



def read_csv(document_path):
    # Document must be Nifty 200 CSV downloaded from NSE
    df = pd.read_csv(document_path)
    return df


def import_sectors_from_csv(dataframe):
    sec = []
    industries = set(dataframe.Industry)
    for industry in industries:
        sec.append(sectors(sector = industry))

    try:
        session.add_all(sec)
        session.commit()
        return "Sectors Successfully Saved"
    except:
        return "Error Saving Sectors"


path = "C:\\Users\\ProfessorVeil\\Desktop\\ind_nifty200list.csv"


def import_stocks_from_csv(dataframe):
    tickers = []
    entries = dataframe[['Company Name', 'Industry', 'Symbol']]

    for header, entries in entries.iterrows():
        company = entries["Company Name"]
        industry = entries["Industry"]
        symbol = entries["Symbol"]

        sectorID = session.query(
            sectors.id,
        ).filter(
            sectors.sector == industry
        ).first()

        check_if_exists = session.query(
            stocks.stock
        ).filter(
            stocks.stock == company
        ).first()

        if not check_if_exists:
            tickers.append(
                stocks(
                    sector_id = sectorID.id,
                    stock = company,
                    symbol = symbol
                )
            )

    try:
        session.add_all(tickers)
        session.commit()
        return "Stocks Successfully Saved"
    except:
        return "Error Saving Stocks"



# import_sectors_from_csv(read_csv(path))
import_stocks_from_csv(read_csv(path))