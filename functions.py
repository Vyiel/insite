import pandas as pd


def toCSV(title: str, data: dict):
    dataFrame = pd.DataFrame.from_dict(data, orient="index")
    dataFrame.to_csv(title + ".csv")




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


print(CurrentAssetsToLiabilities([139891000, 107450000, 73998000, 64357000], [44869000, 33325000, 21552000,16660000]))







