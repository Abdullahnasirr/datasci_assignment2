import string

with open("sample-file", "r") as file: #Opens in read mode
    content = file.read().lower() #converts all text to lowercase



tokens = content.split() #splits all the text into raw tokens based on whitespace

clean_tokens = []
for word in tokens:
    clean_word = word.strip(string.punctuation) #gets rid of punctaution then keeps atleast 2 characters

    if sum(char.isalpha() for char in clean_word) >= 2:
        clean_tokens.append(clean_word)

bigrams = []
# pairs the consecutive cleaned tokens
for i in range(len(clean_tokens) - 1):
    bigrams.append(clean_tokens[i] + " " + clean_tokens[i + 1])


bigram_counts = {}
#Counts how many times each bigram appears
for bigram in bigrams:
    if bigram in bigram_counts:
        bigram_counts[bigram] += 1
    else:
        bigram_counts[bigram] = 1
#Sort bigrams by frequency in descending order
top_5 = sorted(bigram_counts.items(), key=lambda x: x[1], reverse=True)[:5]

for bigram, count in top_5:
    print(f"{bigram} -> {count}") #Prints the top 5 bigrams
