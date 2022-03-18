# The entered number is smallest 4 digits number or not

number = int(input("Enter a number:"))
if(number>1000 and number<9999):
    print("Given number is four digit number")
else:
    print("Given number is not a four digit number")