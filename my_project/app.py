# Step 1: Load data
data = []

with open("data.txt") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            data.append(line)

# Step 2: Search function (ADD YOUR CODE HERE)
def search(query):
    query_words = query.lower().split()
    best_match = None
    max_score = 0

    for item in data:
        item_words = item.lower().split()

        score = 0
        for word in query_words:
            if word in item_words:
                score += 1

        if score > max_score:
            max_score = score
            best_match = item

    # Condition handling
    if max_score == len(query_words):
        return best_match
    elif max_score > 0:
        return f"Closest match found: {best_match}"
    else:
        return "No relevant data found"

# Step 3: Take user input
query = input("Enter crop and soil: ")

# Step 4: Call function
result = search(query)

# Step 5: Print result
print("\n🔍 Result:")
print(result)