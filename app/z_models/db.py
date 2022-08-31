# import psycopg
from dotenv import dotenv_values

# uri = f'postgresql://{credentials['USER']}:{credentials['PASSWORD']}@{credentials['IP']}:{credentials['PORT']}/{credentials['DBNAME']}'

# test_query = 'SELECT * FROM movie WHERE m_id=4'

# with psycopg.connect(conninfo=uri) as conn:
#     with conn.cursor() as cur:
#         cur.execute(test_query)
#         # a = cur.fetchone()
#         # print(cur)


class Database:

    def __init__(self) -> None:
        credentials = dotenv_values('.db_env')

        self.user = credentials['USER']
        self.password = credentials['PASSWORD']
        self.host = credentials['HOST']
        self.port = credentials['PORT']
        self.dbname = credentials['DBNAME']

        self.conn = None

    def connect(self):
        """Connect to DB if not already connected"""
        if self.conn is None:
            try:
                self.conn = psycopg.connect(
                    host = self.host,
                    user = self.user,
                    password = self.password,
                    port = self.port,
                    dbname = self.dbname
                )
            except psycopg.DatabaseError as e:
                print(e)
                raise e
            finally:
                print('Connection opened successfully')
                return self.conn
            

