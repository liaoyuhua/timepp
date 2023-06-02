"""
Generate time series features from raw data.
"""
import pandas as pd


class TimeFeatures:
    freq = ("s", "t", "h", "d", "w", "m", "y")

    def __init__(
        self,
        data: pd.DataFrame,
        time_col: str,
        freq: str = "h",
    ) -> None:
        """
        Args:
            data (pd.DataFrame):
            time_col (str):
            freq (str):
        """
        assert time_col in data.columns, f"{time_col} not in data.columns"
        assert freq in self.freq, f"{freq} not in {self.freq}"
        self.data = data
        self.time_col = time_col
        self.freq = freq

    def extract(self):
        """
        Extract time series features.
        """
        pass
