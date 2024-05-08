from itertools import combinations

# Sample items (you can replace with your actual items)
items = ["A", "B", "C", "D", "E"]

# Generate all possible 1-itemsets
one_itemsets = [(item,) for item in items]

# Generate all possible 2-itemsets
two_itemsets = list(combinations(items, 2))

# Generate all possible 3-itemsets
three_itemsets = list(combinations(items, 3))

# Assume some sample transactions (you can replace with your actual data)
transactions = [
    ["A", "B", "C"],
    ["A", "C", "D"],
    ["B", "C", "E"],
    # ... add more transactions
]

# Calculate support threshold (you can adjust this based on your data)
support_threshold = 2

# Check if each itemset is frequent
frequent_itemsets = []
for itemset in one_itemsets + two_itemsets + three_itemsets:
    count = sum(1 for transaction in transactions if all(item in transaction for item in itemset))
    if count >= support_threshold:
        frequent_itemsets.append((itemset, count))

# Print frequent itemsets
for itemset, count in frequent_itemsets:
    print(f"Frequent itemset {itemset}: Support count = {count}")

# Generate association rules (you can extend this part)
for itemset, count in frequent_itemsets:
    if len(itemset) > 1:
        for i in range(1, len(itemset)):
            antecedent = itemset[:i]
            consequent = itemset[i:]
            print(f"Association rule: {antecedent} => {consequent}")
