from fuzzywuzzy import process

choices = ["apple", "banana", "orange", "pineapple"]
query = "appel"

best_match = process.extractOne(query, choices)
print("Best match for '{}': {}".format(query, best_match[0]))
print("Similarity Ratio: {}%".format(best_match[1]))
