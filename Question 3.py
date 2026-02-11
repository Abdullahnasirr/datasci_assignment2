import string

groups = {}

with open("sample-file", "r") as file:
    for line_number, line in enumerate(file, start=1):

        original_line = line.rstrip("\n")

        #makes it lowercase, removes punctuation, removes whitespace
        normalized = original_line.lower()
        normalized = normalized.translate(str.maketrans("", "", string.punctuation))
        normalized = "".join(normalized.split())

        #Group the lines by form

        groups.setdefault(normalized, []).append((line_number, original_line))

#Keep only almost duplicate sets
duplicate_sets = [group for group in groups.values() if len(group) >= 2]

#Prints a number of near-duplicate sets
print(len(duplicate_sets))

#Prints the first two sets
for i, dup_set in enumerate(duplicate_sets[:2], start=1):
    print(f"\nSet {i}:")
    for line_number, line in dup_set:
        print(f"{line_number}: {line}")
