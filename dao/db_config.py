import sqlite3
import psycopg2
# path / url de conexão
DB_PATH = "postgresql://neondb_owner:npg_MDElQSzfU2i6@ep-summer-violet-acwc2vxb-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
    conn = psycopg2.connect(DB_PATH)
    return conn

