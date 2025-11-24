import string

with open("input.txt", "r", encoding="utf-8") as infile, \
     open("output.txt", "w", encoding="utf-8") as outfile:
    
    for line in infile:
        punct_count = sum(1 for char in line if char in string.punctuation)
        outfile.write(f"{punct_count}\n")

print("Результаты подсчёта знаков препинания записаны в output.txt")