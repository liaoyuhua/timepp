import pandas as pd
from timepp.utils import read_csv_file


class Preprocess:
    def __init__(self, data: pd.DataFrame) -> None:
        pass

    @staticmethod
    def _read_csv(filename):
        """ """
        return read_csv_file(filename)

    @classmethod
    def from_csv(cls, filename, **kwargs):
        """
        Args:
            filename (str):

        """
        data = pd.read_csv(filename, **kwargs)
        return cls(data)

    @classmethod
    def from_pandas(cls, data: pd.DataFrame):
        return cls(data)

    def get_summary(self):
        pass

    def extract_features(self):
        pass
