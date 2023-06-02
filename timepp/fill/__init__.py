"""
Fill missing time steps in time series.
"""
import pandas as pd


def fill_missing_time_steps(
    data: pd.DataFrame, start: str, end: str, freq: str = "D"
) -> pd.DataFrame:
    """
    Fill missing time steps in time series.

    Args:
        data (pd.DataFrame): Dataframe with time series.
        start (str): Start date.
        end (str): End date.
        freq (str): Frequency of the time series. Defaults to "D" (daily).

    Returns:
        pd.DataFrame: Dataframe with filled time steps.

    """
    assert isinstance(data, pd.DataFrame), "Data must be a pandas DataFrame."
    assert isinstance(start, str), "Start must be a string."
    assert isinstance(end, str), "End must be a string."
    assert isinstance(freq, str), "Frequency must be a string."

    data.index = pd.DatetimeIndex(data.index)
    data = data.reindex(pd.date_range(start=start, end=end, freq=freq), fill_value=0)
    return data


def auto_fill_missing_time_steps(data: pd.DataFrame, freq: str = "D") -> pd.DataFrame:
    """
    Automatically fill missing time steps in time series.

    Args:
        data (pd.DataFrame): Dataframe with time series.
        freq (str): Frequency of the time series. Defaults to "D" (daily).

    Returns:
        pd.DataFrame: Dataframe with filled time steps.

    """
    assert isinstance(data, pd.DataFrame), "Data must be a pandas DataFrame."
    assert isinstance(freq, str), "Frequency must be a string."

    start = data.index.min()
    end = data.index.max()
    return fill_missing_time_steps(data, start, end, freq)
