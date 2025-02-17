import pytest
import sqlite3
# define a reusable setup for testing
@pytest.fixture
def db_connection():
    """_connect to the database: orders.db_
    """
    con = sqlite3.connect ("orders.db")
    cur = con.cursor()
    yield cur
    con.close ()

def test_table_orders_exist (db_connection):
    """_Test if table orders exist_
    """
    table = db_connection.execute('''SELECT name FROM sqlite_master \
        WHERE type = 'table' AND name= 'orders' ;''').fetchone()
    assert table is not None, "Table orders exist in the database"

def test_table_not_exist (db_connection):
    """_Test if table abd not exist_
    """
    table = db_connection.execute('''SELECT name FROM sqlite_master \
        WHERE type = 'table' AND name= 'abc' ;''').fetchone()
    assert table is None, "Table abd is not exist in the database, or connection failed"

def test_create_a_table (db_connection):
    """_create table tqh in database_

    Args:
        db_connection (_function/fixture_): _function name_
    """
    db_connection.execute ('''CREATE TABLE tqh (id INTEGER PRIMARY KEY, name TEXT);''')
    table = db_connection.execute('''SELECT name FROM sqlite_master \
        WHERE type = 'table' AND name= 'tqh' ;''').fetchone()
    assert table is not None, "Table tqh exist in the database"
    db_connection.execute ('''DROP TABLE tqh;''')
    
def test_drop_a_table (db_connection):
    """_drop table cht in database_

    Args:
        db_connection (_function/fixture_): _function name_
    """
    db_connection.execute ('''CREATE TABLE cht (id INTEGER PRIMARY KEY, name TEXT);''')
    db_connection.execute ('''DROP TABLE cht;''')
    table = db_connection.execute('''SELECT name FROM sqlite_master \
        WHERE type = 'table' AND name= 'cht' ;''').fetchone()
    assert table is None, "Table cht is not exist in the database, or connection failed"
    
    
