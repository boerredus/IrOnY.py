#!/usr/bin/python3
import sys

txt = list(sys.argv[1] if len(sys.argv) > 1 else input("Text to ironize: "))
for i in range(len(txt)):
    if txt[i] == ' ':
        continue

    txt[i] = txt[i].upper() if i % 2 == 0 else txt[i].lower()
print("".join(txt))
