import pandas as pd
from schema import *


def toCSV(title: str, data: dict):
    dataFrame = pd.DataFrame.from_dict(data, orient="index")
    dataFrame.to_csv(title + ".csv")


def toSQL(symbol: str, title:str, data: dict):

    saveYearlyIncome = []
    saveQuarterlyIncome = []
    saveYearlyBalanceSheet = []
    saveQuarterlyCashFlow = []

    stockID = session.query(
        stocks.id,
    ).filter(
        stocks.symbol == symbol
    ).first()

    if title == "yearlyIncome":

        for particulars, values in data.items():
            check_if_exists = session.query(
                yearlyIncome.stocks_id,
                yearlyIncome.particulars,
            ).filter(
                yearlyIncome.stocks_id == stockID.id,
                yearlyIncome.particulars == particulars
            ).first()

            try:
                y5 = values[0]
            except:
                y5 = None
            try:
                y4 = values[1]
            except:
                y4 = None
            try:
                y3 = values[2]
            except:
                y3 = None
            try:
                y2 = values[3]
            except:
                y2 = None
            try:
                y1 = values[4]
            except:
                y1 = None

            if not check_if_exists:
                saveYearlyIncome.append(
                    yearlyIncome(
                        stocks_id = stockID.id,
                        particulars = particulars,
                        y5 = y5,
                        y4 = y4,
                        y3 = y3,
                        y2 = y2,
                        y1 = y1
                    )
                )

        session.add_all(saveYearlyIncome)
        session.commit()


    if title == "quarterlyIncome":

        for particulars, values in data.items():
            check_if_exists = session.query(
                quarterlyIncome.stocks_id,
                quarterlyIncome.particulars,
            ).filter(
                quarterlyIncome.stocks_id == stockID.id,
                quarterlyIncome.particulars == particulars
            ).first()

            try:
                q6 = values[0]
            except:
                q6 = None
            try:
                q5 = values[1]
            except:
                q5 = None
            try:
                q4 = values[2]
            except:
                q4 = None
            try:
                q3 = values[3]
            except:
                q3 = None
            try:
                q2 = values[4]
            except:
                q2 = None
            try:
                q1 = values[5]
            except:
                q1 = None


            if not check_if_exists:
                saveQuarterlyIncome.append(
                    quarterlyIncome(
                        stocks_id = stockID.id,
                        particulars = particulars,
                        q6 = q6,
                        q5 = q5,
                        q4 = q4,
                        q3 = q3,
                        q2 = q2,
                        q1 = q1,
                    )
                )

        session.add_all(saveQuarterlyIncome)
        session.commit()


    if title == "yearlyBalanceSheet":

        for particulars, values in data.items():
            check_if_exists = session.query(
                balanceSheet.stocks_id,
                balanceSheet.particulars,
            ).filter(
                balanceSheet.stocks_id == stockID.id,
                balanceSheet.particulars == particulars
            ).first()

            try:
                y4 = values[0]
            except:
                y4 = None
            try:
                y3 = values[1]
            except:
                y3 = None
            try:
                y2 = values[2]
            except:
                y2 = None
            try:
                y1 = values[3]
            except:
                y1 = None

            if not check_if_exists:
                saveYearlyBalanceSheet.append(
                    balanceSheet(
                        stocks_id = stockID.id,
                        particulars = particulars,
                        y4 = y4,
                        y3 = y3,
                        y2 = y2,
                        y1 = y1,
                    )
                )

        session.add_all(saveYearlyBalanceSheet)
        session.commit()


    if title == "yearlyCashFlow":

        for particulars, values in data.items():
            check_if_exists = session.query(
                yearlyCashflow.stocks_id,
                yearlyCashflow.particulars,
            ).filter(
                yearlyCashflow.stocks_id == stockID.id,
                yearlyCashflow.particulars == particulars
            ).first()

            try:
                y4 = values[0]
            except:
                y4 = None
            try:
                y3 = values[1]
            except:
                y3 = None
            try:
                y2 = values[2]
            except:
                y2 = None
            try:
                y1 = values[3]
            except:
                y1 = None

            if not check_if_exists:
                saveQuarterlyCashFlow.append(
                    yearlyCashflow(
                        stocks_id = stockID.id,
                        particulars = particulars,
                        y4 = y4,
                        y3 = y3,
                        y2 = y2,
                        y1 = y1,
                    )
                )

        session.add_all(saveQuarterlyCashFlow)
        session.commit()



def trendMapBasic(data: list):
    """
    If given a list of numbers, the function would calculate if the numbers are moving in an upward or downward trajectory.
    Reason for reversing is that the data will be provided from current - trailing years format, whereas I would need to
    calculate the SMA based from the starting quarter or year.
    """

    data.reverse()

    numbers = []
    total = 0
    iterator = 0
    sma = []
    trail = 0
    trend = None
    mode = None

    for i in data:
        try:
            i = float(i)
        except ValueError:
            i = float(0)
        numbers.append(i)

    for i in numbers:
        iterator += 1
        total = total + i
        sma.append(total / iterator)

    if sma[-1] > sma[-2]:
        trend = "Positive"
        for i in range(1, len(sma)):
            if sma[-i] > sma[-(i + 1)]:
                trail += 1
            else:
                break

        if sma[-1] < 0:
            mode = "Recovery"

    elif sma[-1] < sma[-2]:
        trend = "Negative"
        for i in range(1, len(sma)):
            if sma[-i] < sma[-(i + 1)]:
                trail += 1
            else:
                break

        if sma[-1] < 0:
            mode = "Downfall"

    return {
        "SMA": sma,
        "Trend": trend,
        "Trail": str(trail) + "/" + str(len(numbers)),
        "Mode": mode
    }


# print(trendMapBasic([-2896000, -17434000, -22752000, -25673000]))
# print(trendMapBasic([400, -150, 200, 100]))


def CurrentAssetsToLiabilities(currentAssets: list, currentLiabilities: list):
    """
    This calculation is referenced from Mark Tilbury, Who says that If the current assets/Current Liabilities > 1, then
    it's that many times, the company can pay their debts off!
    """

    AssetsToLiabilities = []

    result_for_current_year_only = round(currentAssets[0]/currentLiabilities[0])

    if len(currentAssets) == len(currentLiabilities):
        for i in range(len(currentAssets)):
            AssetsToLiabilities.append(currentAssets[i]/currentLiabilities[i])

    if result_for_current_year_only > 1:
        nature = "Positive"
    else:
        nature = "Negative"

    trends = trendMapBasic(AssetsToLiabilities)

    return {
        "CurrentAssetToLiabilities": result_for_current_year_only,
        "Nature": nature,
        "SMA": trends['SMA'],
        "Trend": trends['Trend'],
        "Trail": trends['Trail'],
        "Mode": trends['Mode']
    }


# print(CurrentAssetsToLiabilities([139891000, 107450000, 73998000, 64357000], [44869000, 33325000, 21552000,16660000]))







