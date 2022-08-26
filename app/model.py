import psycopg
from dotenv import dotenv_values

credentials = dotenv_values(".env")
uri = f'postgresql://{credentials["USER"]}:{credentials["PASSWORD"]}@{credentials["IP"]}:{credentials["PORT"]}/{credentials["DBNAME"]}'

test_query = 'SELECT * FROM movie WHERE m_id=4'

with psycopg.connect(conninfo=uri) as conn:
    with conn.cursor() as cur:
        cur.execute(test_query)
        a = cur.fetchone()
        # print(cur)
        print(a)
