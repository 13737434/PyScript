
text=''
with open('test.txt', 'r') as f:
    text=f.read()
print(text)

file = open('test.c', 'w')
file.write(text)