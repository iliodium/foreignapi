import os

from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

DATABASE_URL_syncpg = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_URL_asyncpg = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

BOOKKEEPING_GRPC_NAME = os.environ.get("BOOKKEEPING_GRPC_NAME")
BOOKKEEPING_REST_NAME = os.environ.get("BOOKKEEPING_REST_NAME")

BOOKKEEPING_GRPC_PORT = os.environ.get("BOOKKEEPING_GRPC_PORT")
BOOKKEEPING_REST_PORT = os.environ.get("BOOKKEEPING_REST_PORT")
