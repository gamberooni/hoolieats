from pathlib import Path

HOOLIEATS_DIR = Path(__file__).parent.absolute()
HOOLIEATS_DBT_DIR = Path(f"{HOOLIEATS_DIR.parent}/hoolieats-dbt")
HOOLIEATS_DUCKDB = Path(f"{HOOLIEATS_DBT_DIR}/hoolieats.duckdb").as_posix()
