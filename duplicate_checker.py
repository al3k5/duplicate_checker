import os

names = os.listdir()
dupes = []

for file in names:
    if str("(2).") in file:
        dupes.append(file)

print(f"\nnumber\t| file_name\n{'-' * 50}\nnon-duplicates\n{'-' * 50}\n")

num = 0

for i in names:
    if i not in dupes:
        print(f"{num}\t - {i}")
        num += 1

if num == 0:
    print("NO NON-DUPLICATES FOUND")

print(f"\n{'-' * 50}\nduplicates\n{'-' * 50}\n")

num = 0

for i in dupes:
    print(f"{num}\t - {i}")
    num += 1

if num == 0:
    print("\nNO DUPLICATES FOUND\n")
    exit()

input("\nPRESS [ENTER] TO MOVE LISTED FILES TO TEMP-DIR")

if os.path.exists("./temp"):
    pass
else:
    os.makedirs("./temp")

for i in dupes:
    os.rename(i, f"./temp/{i}")