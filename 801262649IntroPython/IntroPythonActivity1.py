#program 1
def stringBothEnds(str):
    if len(str) < 2 :
        return "Your String is too short! "
    return str[0:2] + str[-2:]  

string1 = input("Please enter a string: ")
string2 = stringBothEnds(string1)
print (string2)
