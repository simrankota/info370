print('hello world')

a = 1
b = 1.0
c = True
d = False

print("true plus one", c + 1)

e = 'a'
f = "a"
g = "I've"
print(g)

print(1 + 2*3)
print(2**3)
# exponentiation
print(7 % 4)
# classic mod function
print(7//4)
# integer division
s = g + ' ' + "no money"
print(s)

x = 1
print("x is " + str(x))

friends = 5
budget = 100.00
print("I am going with " + str(friends) + " friends")
cost = 15.00
total = cost * friends
total = total * 1.15
if total < budget:
    print("can afford")
else:
    print ("cannot afford")

a = 1
def multiply(x, y=2):
    z = x*y
    global a
    # must explicitly declare globals
    print("a inside 'multiply'", a)
    a = 2
    return z

# print(multiply(3, 4))
print(multiply(3))
print('a outside "multiply"', a)

for i in range(10):
    print(i)
    if i > 4:
        break

l = [1, 2.0, 'xyz']
print("our list:\n", l)
l1 = ['pizza', 'fried chicken', 'french fries', 'donuts', 'spaghetti', 'pasta']
print(l1)
print(l1[0])
print(l1[2])
print(l1[2:5])
print(l1[2:])
print(l1[:5])
print(l1[-1])
print(l1[1:5:2])
# step size of 2
print(l1[::2])
# first to last step size 2
print(l1[::-1])
# first to last in reverse order (flip)
l2 = l1
# shallow copy, just copies a pointer, doesn't take any more memory
# deep copy makes a new identical object, takes a lot of memory
l2[0] = "merlot"
print(l1)
l2 = l1.copy()
# makes a deep copy
l2[1] = "chardonnay"
print(l2)
print(l1)

l3 = l1 + l2
# concatenates lists
print(l3)
a = []
a.append(1)
# add to end of list
print(a)
a.append([2, 3])
print(a)

near = ["Person 1", "Ott"]
not_near = []
for i in ["Ansul", "Harini"]:
    not_near.append(i)
new = near + not_near
print("All the names:\n" + str(new))

print([i**2 for i in range(10)])
# list comprehension: function applies to for loop, creates list out of results
print([1 / x * x - 1 for x in range(1, 101)])
# range(start, end + 1)

d = {'name': 'Kong Ming', 'power': 7}
print('dict:', d)
print({i:i**2 for i in range(10)})
# same as list comprehension
print({x: 1 / x * x - 1 for x in range(1,101)})