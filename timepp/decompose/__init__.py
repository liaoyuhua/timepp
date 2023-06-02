"""
Decompose time series into components.
Look for more information on the following links:
https://otexts.com/fpp2/classical-decomposition.html
"""
from copy import copy
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose, STL


class Decomposer:
    methods = ("basic", "stl")

    def __init__(self, data: pd.DataFrame, y: str) -> None:
        assert y in data.columns, f"Column {y} not in data."
        self.data = data
        self.y = y

    def basic(
        self,
        method: str = "additive",
        period: int = None,
        plot: bool = False,
        inplace: bool = False,
    ) -> pd.DataFrame:
        """
        Decompose time series into seasonal, trend and residual components.

        Args:
            method (str): Method to use for decomposition. Can be "additive" or "multiplicative".
            period (int): Period of the time series. If not provided, it will be inferred from the index.
            plot (bool): Whether to plot the decomposition or not.
            inplace (bool): Whether to add the components to the data or not.

        Returns:
            pd.DataFrame: DataFrame with the components.
        """
        assert method in (
            "additive",
            "multiplicative",
        ), f"Method {method} not supported."

        assert (
            self.data.index.freq is not None or period is not None
        ), "Data must have a frequency."

        if method == "additive":
            decomposition = seasonal_decompose(
                self.data[self.y], model="additive", period=period
            )
        elif method == "multiplicative":
            decomposition = seasonal_decompose(
                self.data[self.y], model="multiplicative", period=period
            )

        if plot:
            decomposition.plot()
            plt.show()

        if inplace:
            data = copy(self.data)
            data["seasonal"] = decomposition.seasonal
            data["trend"] = decomposition.trend
            data["residual"] = decomposition.resid
            return data
        else:
            return pd.DataFrame(
                {
                    "seasonal": decomposition.seasonal,
                    "trend": decomposition.trend,
                    "residual": decomposition.resid,
                }
            )

    def stl(
        self,
        period: int = None,
        robust: bool = True,
        plot: bool = False,
        inplace: bool = False,
    ) -> pd.DataFrame:
        """
        Decompose time series into components.

        Args:
            period (int): Period of the time series. If not provided, it will be inferred from the index.
            robust (bool): Whether to use robust decomposition or not.
            plot (bool): Whether to plot the decomposition or not.
            inplace (bool): Whether to add the components to the data or not.

        Returns:
            pd.DataFrame: DataFrame with the components.
        """
        assert (
            self.data.index.freq is not None or period is not None
        ), "Data must have a frequency."

        decomposition = STL(self.data[self.y], period=period, robust=robust).fit()

        if plot:
            decomposition.plot()
            plt.show()

        if inplace:
            data = copy(self.data)
            data["seasonal"] = decomposition.seasonal
            data["trend"] = decomposition.trend
            data["residual"] = decomposition.resid
            return data
        else:
            return pd.DataFrame(
                {
                    "seasonal": decomposition.seasonal,
                    "trend": decomposition.trend,
                    "residual": decomposition.resid,
                }
            )
