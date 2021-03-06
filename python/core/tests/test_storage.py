"""Tests for `poc-multi-api` package."""
import pandas as pd
from poccore import storage


def test_avg_price(df_prices, input_path, output_path):
    df_prices.to_parquet(input_path)

    groupby = "brand"
    field = "price"

    status = storage.avg_price(
        input_path=input_path,
        output_path=output_path,
        groupby=groupby,
        field=field,
    )

    assert status

    result = pd.read_parquet(output_path)

    for brand in ["brand1", "brand2"]:
        assert result[result[groupby] == brand][field].values[0] == 20000
