'''import all necessary to test'''
import pytest
import sqlite3
import os
from app import another_select_a_column, another_index

@pytest.fixture
def db_connection():
    """Connect to the database: orders.db in the MenuStore folder."""
    # Use the relative path from the BurgerOrderer folder to MenuStore
    db_path = os.path.join(os.path.dirname(__file__), '..', 'MenuStore', 'orders.db')
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    yield cur
    con.close()

def test_select_a_column():
    """_test function select_a_column in BurgeOrderer _
    """
    db_path = os.path.join(os.path.dirname(__file__), '..', 'MenuStore', 'orders.db')
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    list_column = another_select_a_column('name', 'burger', cur)
    assert list_column ==  [('cheese burger',), ('fish burger',), ('vegan burger',)]

def test_index ():
    """_test function index in BurgerOrderer_
    """
    db_path = os.path.join(os.path.dirname(__file__), '..', 'MenuStore', 'orders.db')
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    lstBurger = another_index ('name', 'burger', cur)
    assert lstBurger ==  (['cheese burger', 'fish burger', 'vegan burger'])
        
