from dataclasses import dataclass
from typing import Optional

from duckdb import DuckDBPyConnection
from pandas import DataFrame


class ReturnType:
    PANDAS_DF = "df"
    NUMPY_ARRAY = "numpy"


@dataclass
class QueryExecutor:
    connection: DuckDBPyConnection

    def execute(
        self, sql: str, return_type: Optional[ReturnType] = ReturnType.PANDAS_DF
    ) -> DataFrame:
        if return_type == ReturnType.PANDAS_DF:
            return self.connection.execute(sql).fetchdf()
        if return_type == ReturnType.NUMPY_ARRAY:
            return self.connection.execute(sql).fetchnumpy()
