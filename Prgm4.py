# Write a program to take input of age of 3 people by user
# and determine oldest and youngest among them

a = int(input("Enter your age1:"))
b = int(input("Enter your age2:"))
c = int(input("Enter your age3:"))
if (a > b and a > c):
    if (b > c):
        print("A is Oldest,C is youngest")
    else:
        print("A is Oldest,B is youngest")
elif (b > c and b > a):
    if (c > a):
        print("b is oldest,A is youngest")
    else:
        print("b is oldest,C is youngest")
elif (c > a and c > b):
    if(a>b):
        print("C is oldest,b is youngest")
    else:
        print("C is oldest, a is youngest")
else:
        print("")


