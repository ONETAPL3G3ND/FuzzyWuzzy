from fuzzywuzzy import fuzz

string1 = "apple pie"
string2 = "apple pye"

similarity_ratio = fuzz.ratio(string1, string2)
print(f"Similarity Ratio between '{string1}' and '{string2}': {similarity_ratio}%")