#import the functions required
from flask import Flask, render_template, request
import sqlite3
import logging

app = Flask(__name__)

# Set up logging to debug
logging.basicConfig(level=logging.INFO,  # Set the logging level
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('app.log'),  # Log to a file
                              logging.StreamHandler()]) 

def select_a_column(column, table_name):
    """Function to select a specific column from a table.

    Args:
        column (str): The column name to select.
        table_name (str): The name of the table to query from.
    """
    with sqlite3.connect('orders.db') as conn:
        cursor = conn.cursor()
        column_table_check = f'SELECT {column} FROM {table_name}'
        cursor.execute(column_table_check)
        lst_column = cursor.fetchall()
    return lst_column

def another_select_a_column(column, table_name, cursor):
    """Function use for BO_test, copy code from def index() but add "cursor"

    Args:
        column (str): The column name to select.
        table_name (str): The name of the table to query from.
    """
    column_table_check = f'SELECT {column} FROM {table_name}'
    cursor.execute(column_table_check)
    lst_column = cursor.fetchall()
    return lst_column

def another_index(column, table, cursor):
    """_Use for BO_test.py, copy code from def index() but add "cursor"_

    Args:
        column (_str_): _column name_
        table (_str_): _table name_
        cursor (_cursor database_): _cursor name_

    Returns:
        _list_: _list burger_
    """
    # Using a context manager for the database connection
    try:
        listBurgerData = another_select_a_column (column, table, cursor)
        # Use list comprehension to fetch and create the list
        listBurger = [name[0] for name in listBurgerData]

    # Handle database errors (optional: log the error, show a message, etc.)
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        listBurger = []  # Set to an empty list if an error occurs

    # To pass listBurger to main_menu.html and render the list of burgers
    return listBurger

# Route for home side. 
@app.route('/')
def index():
    # Using a context manager for the database connection
    try:
        listBurgerData = select_a_column ('name', 'burger')
        # Use list comprehension to fetch and create the list
        listBurger = [name[0] for name in listBurgerData]

    # Handle database errors (optional: log the error, show a message, etc.)
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        listBurger = []  # Set to an empty list if an error occurs

    # To pass listBurger to main_menu.html and render the list of burgers
    return render_template('main_menu.html', listBurger=listBurger)

# Route for topping side. 
@app.route('/topping', methods=['POST'])
def topping():
    burger = request.form.get('burger')
    print (burger)
    # Using a context manager for the database connection
    try:
        # Get data of all options in database.
        listItems = select_a_column ('*', 'items')

        # Filter items based on their type and action
        listExtraItem = [item[1] for item in listItems if item[2] == 'ITEMS' and item[3] == 'ADD']
        listTopping = [item[1] for item in listItems if item[2] == 'ITEMS' and item[3] == 'REMOVE']
        listSideOption = [item[1] for item in listItems if item[2] == 'SIDES' and item[3] == 'ADD']
        listDrink = [item[1] for item in listItems if item[2] == 'DRINKS' and item[3] == 'ADD']
    
    # Handle database errors (optional: log the error, show a message, etc.)    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        listItems = []  # Set to an empty list if an error occurs
    
    # To pass all options to main_menu.html and render the list of all options
    return render_template('topping.html', 
                           burger=burger, 
                           listExtraItem=listExtraItem, 
                           listTopping=listTopping, 
                           listSideOption=listSideOption, 
                           listDrink=listDrink)
    
# Collect the order. 
@app.route('/order_done', methods=['POST'])
def done():
    form_data = request.form
    app.logger.info("Form Data: %s", form_data)
    # retrieves form data from an HTTP POST request 
    # and prints the values for debugging purposes
    burger = form_data.get('burger')
    added_items = form_data.get('added_items')
    removed_items = form_data.get('removed_items')
    added_sides = form_data.get('added_sides')
    drinks = form_data.get('drinks')
    
    # Print for debug
    app.logger.info("Burger: %s", burger)
    app.logger.info("Added Items: %s", added_items)
    app.logger.info("Removed Items: %s", removed_items)
    app.logger.info("Added Sides: %s", added_sides)
    app.logger.info("Drinks: %s", drinks)

    # Save order in the database
    try:
        with sqlite3.connect('orders.db') as conn:
            cursor = conn.cursor()

            # Insert order and get order_id
            cursor.execute('INSERT INTO orders (status) VALUES (?)', ('Not done',))
            order_id = cursor.lastrowid
            app.logger.info("Order_ID: %s",order_id)
            burger = burger.lower()
            app.logger.info("Burger_lower: %s",burger)
            
            
            # Insert burger into order_burger
            cursor.execute('SELECT * from burger WHERE name = ?', (burger,))
            burger_object = cursor.fetchone()
            burger_id = burger_object[0]
            app.logger.info("Burger_object[0]: %s",burger_object[0])
            cursor.execute('INSERT INTO order_burger (order_id, burger_id) VALUES (?, ?)', 
                       (order_id, burger_id,))
            
            # Insert added items
            added_item_id = get_item_id(cursor, 'ITEMS', added_items, 'ADD')
            insert_order_item(cursor, order_id, burger_id, added_item_id)
            app.logger.info("Added_item_id: %s", added_item_id)
            

            # Insert removed items
            removed_item_id = get_item_id(cursor, 'ITEMS', removed_items, 'REMOVE')
            insert_order_item(cursor, order_id, burger_id, removed_item_id)
            app.logger.info("Remove_item_id: %s",removed_item_id)

            # Insert added sides
            side_id = get_item_id(cursor, 'SIDES', added_sides, 'ADD')
            insert_order_item(cursor, order_id, burger_id, side_id)
            app.logger.info("Side_id: %s",side_id)
            

            # Insert drinks
            drink_id = get_item_id(cursor, 'DRINKS', drinks, 'ADD')
            insert_order_item(cursor, order_id, burger_id, drink_id)
            app.logger.info("Drink_id: %s",drink_id)

            conn.commit()
        
    # Handle database errors (optional: log the error, show a message, etc.)
    except sqlite3.Error as e:
        app.logger.error("Database error: %s", e)
        return render_template('error.html', error=str(e))

    return render_template('order_done.html')

def get_item_id(cursor, item_type, item_name, action=None):
    """
    Fetch item ID from the database based on item type, name, and optionally action.
    If action is provided, it fetches the item with the given action.
    """
    if action is not None:
        cursor.execute('SELECT id FROM items WHERE name = ? AND type = ? AND action = ?', 
                       (item_name, item_type, action))
    else:
        cursor.execute('SELECT id FROM items WHERE name = ? AND type = ?', 
                       (item_name, item_type))
    record = cursor.fetchone()
    return record[0] if record else None

def insert_order_item(cursor, order_id, burger_id, item_id=None):
    """
    Insert an item into the order_burger table.
    This now also stores the action (ADD, REMOVE) along with the order.
    """
    cursor.execute('INSERT INTO order_burger (order_id, burger_id, items_id) VALUES (?, ?, ?)', 
                       (order_id, burger_id, item_id))
   
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
    
