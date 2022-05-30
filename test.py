import txt

with open('category.txt') as file:
    reader=txt.reader(file)
    for line in reader:
        print(line)