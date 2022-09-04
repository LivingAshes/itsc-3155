#program 2
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))
str1 = ("")
for x in range(num1, num2):
    if (x % 7) == 0 :
        if (x % 5) != 0 :
            str1 = str1 + str(x) + ","
print (str1)