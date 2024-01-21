import psycopg2
from psycopg2.extras import LogicalReplicationConnection

# LogicalReplicationConnection
connection = psycopg2.connect(connection_factory=LogicalReplicationConnection)

# cursor
cur = connection._cursor()
