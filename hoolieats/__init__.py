import duckdb
from constants import HOOLIEATS_DUCKDB
from models import QueryExecutor

conn = duckdb.connect(database=HOOLIEATS_DUCKDB, read_only=True)
query_executor = QueryExecutor(conn)
