words = []
word = input("Enter a word (blank line to quit): ")

while word != "":
    if word not in words:
        words.append(word)
    
    word = input("Enter a word (blank line to quit): ")

print(words)
