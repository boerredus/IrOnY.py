#!/usr/bin/python3

txt = list(input("Text to ridicule: "))
for i in range(len(txt)):
    if i % 2 == 0:
        txt[i] = txt[i].upper()
    else:
        txt[i] = txt[i].lower()
print("\n\n", "".join(txt))