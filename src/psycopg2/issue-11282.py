import psycopg2
from psycopg2._psycopg import cursor, ReplicationCursor as _psycopg_ReplicationCursor, ReplicationConnection
from psycopg2.extras import LogicalReplicationConnection, ReplicationCursor


def some():
    # LogicalReplicationConnection
    connection = psycopg2.connect(connection_factory=ReplicationConnection)

    # cursor
    cur = connection.cursor()


print(issubclass(ReplicationCursor, cursor))
print(issubclass(_psycopg_ReplicationCursor, cursor))
