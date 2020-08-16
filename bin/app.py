#!/usr/bin/python3

txt = list(input("Text to ironize: "))
for i in range(len(txt)):
    if txt[i] == ' ':
        continue
        
    txt[i] = txt[i].upper() if i % 2 == 0 else txt[i].lower()
print("\n\n", "".join(txt))
