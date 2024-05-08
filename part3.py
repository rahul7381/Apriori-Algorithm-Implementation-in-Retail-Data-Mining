import pandas as pd
from efficient_apriori import apriori
from fpgrowth_py import fpgrowth
import time

# User input: Set support and confidence thresholds
min_support = 0.1  # Adjust as needed
min_confidence = 0.5  # Adjust as needed

# Load transaction data (replace with your actual data)
def load_transactions(csv_file):
    df = pd.read_csv(csv_file)
    # Ensure all items are strings
    transactions = [set(str(item) for item in row.dropna()) for _, row in df.iterrows()]
    return transactions

transactions_db1 = load_transactions("transactions_db1.csv")
transactions_db2 = load_transactions("transactions_db2.csv")
# Repeat for other databases

# Apriori algorithm
start_time = time.time()
itemsets, rules_apriori = apriori(transactions_db1, min_support=min_support, min_confidence=min_confidence)
end_time = time.time()
print(f"Apriori execution time: {end_time - start_time:.4f} seconds")

# FP-growth algorithm
start_time = time.time()
freqItemSet, rules_fpgrowth = fpgrowth(transactions_db1, minSupRatio=min_support, minConf=min_confidence)
end_time = time.time()
print(f"FP-growth execution time: {end_time - start_time:.4f} seconds")

# Print association rules
print("\nApriori Rules:")
for rule in rules_apriori:
    print(rule)

print("\nFP-growth Rules:")
for rule in rules_fpgrowth:
    print(rule)

# Compare results (you can add more comparison logic if needed)
if len(rules_apriori) == len(rules_fpgrowth):
    print("\nBoth algorithms produced the same number of rules.")
else:
    print("\nAlgorithms produced different numbers of rules.")
