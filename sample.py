def square(num):
    return num ** 2

x = [1, 2, 3, 4, 5]
s1 = []

for i in x:
    s1.append(square(i))

print(s1)
# .................................

def square(num):
    return num ** 2

x = [1, 2, 3, 4, 5]

# using map function
s2 = list(map(square, x))
print(s2)
print(x)

# .......................................


x = [1, 2, 3, 4, 5]
s3 = []

for i in x:
    s3.append(i**2)

print(s3)
