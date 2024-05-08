import csv
import random
from datetime import date, timedelta

# List of items
items = [
    "Diapers",
    "Milk",
    "Bread",
    "Eggs",
    "Apples",
    "Cereal",
    "Toilet Paper",
    "Pasta",
    "Soap",
    "Chips"
]

# Generate transactions for multiple databases
num_databases = 5
num_transactions_per_db = 20

for db_id in range(1, num_databases + 1):
    transactions = []
    for transaction_id in range(1, num_transactions_per_db + 1):
        transaction_date = (date.today() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
        item = random.choice(items)
        quantity = random.randint(1, 5)
        price = round(random.uniform(1.0, 10.0), 2)
        transactions.append((transaction_id, transaction_date, item, quantity, f"{price:.2f}"))

    # Save transactions to CSV
    csv_filename = f"transactions_db_{db_id}.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Transaction ID", "Date", "Item", "Quantity", "Price"])
        writer.writerows(transactions)

    print(f"Database {db_id} transactions saved to {csv_filename}")
