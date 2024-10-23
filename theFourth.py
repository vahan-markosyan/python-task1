text = input("please enter a word")
dzaynavorener = "aeouiAEOUI"
count = 0
for i in text:
    if i in dzaynavorener:
        count += 1

print(count)        