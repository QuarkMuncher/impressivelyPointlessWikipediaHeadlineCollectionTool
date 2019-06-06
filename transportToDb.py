# This code is likely only used once to
# port the gathered data from a textfile'
# into a database.

# [[ IMPORTS ]]
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy_utils import database_exists, create_database
import settings as s

engine = create_engine(
    f"{s.DB_DRIVER}://{s.DB_USER}:{s.DB_PASSWORD}@{s.DB_SERVER}/{s.DB_NAME}",
    echo=True,
)
meta = MetaData()
wikilist = Table(
    "wikilist",
    meta,
    Column("id", Integer, primary_key=True),
    Column("headline", String(100)),
)

if not database_exists(engine.url):
    create_database(engine.url)

meta.create_all(engine)

with open("TheMeaningOfLife.txt") as f:
    f_list = f.read().splitlines()
    print(f_list[1])
    conn = engine.connect()
    for l in f_list:
        ins = wikilist.insert().values(headline=l)
        # ins.bind(conn)
        ins.compile()
        conn.execute(ins)

# connection.execute("commit")
