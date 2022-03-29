largest = 0
book = ""

with open("books_and_chapters.txt") as books:
    for line in books:
        [a,b,c] = line.split(":")
        if int(b) > largest:
            largest = int(b)
            book = a
    
print("The longest book is " + book + " at " + str(largest) + " chapters long.")