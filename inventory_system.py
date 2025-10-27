import logging
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

stock_data = {}

def add_item(item, qty=0):
    """Add an item to inventory."""
    if not isinstance(qty, int) or qty < 0:
        logging.warning(f"Invalid quantity '{qty}' for item '{item}'")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logging.info(f"Added {qty} units of {item} (total: {stock_data[item]})")

def remove_item(item):
    """Remove an item from inventory."""
    try:
        del stock_data[item]
        logging.info(f"Removed item: {item}")
    except KeyError:
        logging.warning(f"Item '{item}' not found in stock")

def load_data():
    """Load inventory data from file."""
    global stock_data
    try:
        with open('inventory.json', 'r', encoding='utf-8') as file:
            stock_data = json.load(file)
            logging.info("Data loaded successfully.")
    except FileNotFoundError:
        logging.warning("No previous inventory data found.")

def save_data():
    """Save inventory data to file."""
    with open('inventory.json', 'w', encoding='utf-8') as file:
        json.dump(stock_data, file, indent=4)
        logging.info("Data saved successfully.")

def print_data():
    """Display current inventory."""
    for item, qty in stock_data.items():
        print(f"{item}: {qty}")

def check_low_items(threshold=5):
    """Check for low-stock items."""
    low_items = {i: q for i, q in stock_data.items() if q < threshold}
    logging.info(f"Low stock items: {low_items}")
    return low_items

if __name__ == "__main__":
    load_data()
    add_item("Apples", 10)
    remove_item("Bananas")
    print_data()
    check_low_items()
    save_data()

