import string

def word_frequencies(filename):
    counts = {}

    #this reads the file

    with open(filename, "r") as file:
        text = file.read()

    #Splits it into tokens
    tokens = text.split()


    for token in tokens:
        # makes it lowercase
        token = token.lower()

        #Removes punctuation from start and end
        token = token.strip(string.punctuation)

        #makes sure tokens keep atleast two characters


        if sum(char.isalpha() for char in token) >= 2:
            counts[token] = counts.get(token, 0) + 1

    #Sorts the  frequency and takes the top 10
    top_10 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]


    #Print  the results
    for word, count in top_10:
        print(f"{word} -> {count}")



word_frequencies("sample-file")
