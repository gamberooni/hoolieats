import os
import sys

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

from utils.common import init_postgres_conn
from config.config import *


def main():
    conn = init_postgres_conn(
        postgres_host,
        postgres_port,
        postgres_database,
        postgres_user,
        postgres_password,
    )
    cur = conn.cursor()
    cur.execute("DROP SCHEMA public CASCADE;")
    cur.execute("CREATE SCHEMA public;")
    conn.commit()
    print("Recreated database")
    conn.close()


if __name__ == "__main__":
    main()
