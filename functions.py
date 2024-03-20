import pandas as pd


def toCSV(title: str, data: dict):
    dataFrame = pd.DataFrame.from_dict(data, orient="index")
    dataFrame.to_csv(title+".csv")


def trendMapBasic(data: list):
    """
    If given a list of numbers, the function would calculate if the numbers are moving in an upward or downward trajectory.
    """

    data.reverse()

    numbers = []
    total = 0
    iterator = 0
    sma = []
    trail = 0
    trend = None


    for i in data:
        try:
            i = int(i)
        except ValueError:
            i = 0

        numbers.append(i)

    for i in numbers:
        iterator += 1
        total = total + i
        sma.append(round(total / iterator))


    if sma[-1] > sma[-2]:
        trend = "Positive"
        for i in range(1, len(sma)):
            if sma[-i] > sma[-(i+1)]:
                trail += 1
            else:
                break

    elif sma[-1] < sma[-2]:
        trend = "Negative"
        for i in range(1, len(sma)):
            if sma[-i] < sma[-(i+1)]:
                trail += 1
            else:
                break


    return {
        "SMA": sma,
        "Trend": trend,
        "Trail": trail
    }





print(trendMapBasic([100, -100, -60, -50]))






