import os

PG_PASSWORD = os.getenv('PG_PASSWORD', 'secret')
PG_USER = os.getenv('PG_USER', 'app')
PG_DB = os.getenv('PG_DB', 'app')
PG_HOST = os.getenv('PG_HOST', 'localhost')
PG_PORT = os.getenv('PG_PORT', '5431')

PG_DSN = f'postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}'