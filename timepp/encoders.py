import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


class Encoder:
    type_to_encoder = {"onehot": OneHotEncoder, "label": LabelEncoder}

    def __init__(self, data: pd.DataFrame, type: str = "onehot") -> None:
        """
        Encoding categorical features.
        """
        self.data = data

        assert type in self.type_to_encoder.keys(), f"Unknown encoder type {type}"
        self.type = type

        self.encoder = self.type_to_encoder[self.type]()

    def fit(self, col: str) -> None:
        """
        Fit the encoder on the column.
        """
        self.encoder.fit(self.data[col].values.reshape(-1, 1))

    def transform(self, col: str) -> np.ndarray:
        """
        Transform the column.
        """
        return self.encoder.transform(self.data[col].values.reshape(-1, 1))

    def fit_transform(self, col: str) -> np.ndarray:
        """
        Fit and transform the column.
        """
        self.fit(col)
        return self.transform(col)

    def inverse_transform(self, col: str) -> np.ndarray:
        """
        Inverse transform the column.
        """
        return self.encoder.inverse_transform(self.data[col].values.reshape(-1, 1))

    def mapping(self, col: str) -> dict:
        """
        Return the mapping from the encoder.
        """
        return dict(
            zip(self.encoder.classes_, self.encoder.transform(self.encoder.classes_))
        )

    def save(self, path: str) -> None:
        """
        Save the encoder.
        """
        pass

    def load(self, path: str) -> None:
        """
        Load the encoder.
        """
        pass


class Normalizer:
    def __init__(self, data: pd.DataFrame) -> None:
        """
        Normalize the data.
        """
        self.data = data
        self.mean = None
        self.std = None

    def fit(self, col: str) -> None:
        """
        Fit the normalizer on the column.
        """
        self.mean = self.data[col].mean()
        self.std = self.data[col].std()

    def transform(self, col: str) -> np.ndarray:
        """
        Transform the column.
        """
        return (self.data[col] - self.mean) / self.std

    def fit_transform(self, col: str) -> np.ndarray:
        """
        Fit and transform the column.
        """
        self.fit(col)
        return self.transform(col)

    def inverse_transform(self, col: str) -> np.ndarray:
        """
        Inverse transform the column.
        """
        return self.data[col] * self.std + self.mean

    def save(self, path: str) -> None:
        """
        Save the normalizer.
        """
        pass

    def load(self, path: str) -> None:
        """
        Load the normalizer.
        """
        pass
