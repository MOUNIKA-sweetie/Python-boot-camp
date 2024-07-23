#input:ABC
#skip 4
#output:EFG
a="ABC"
b=" "
for i in a:
  b=(+chr(ord(i)+4))
print(b)