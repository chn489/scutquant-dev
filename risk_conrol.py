import pandas as pd


def delta(fund: pd.Series, index: pd.Series) -> float:
    """
    在单指数模型下, delta = beta, beta为index对fund回归的系数
    在一个移动窗口(5)内的delta

    :param fund: pd.Series基金收益率
    :param index: pd.Series指数收益率
    :return: float
    """
    rolling_cov = fund.rolling(5).cov(index)
    rolling_var = fund['Column A'].rolling(5).var()
    beta = rolling_cov / rolling_var
    return beta
