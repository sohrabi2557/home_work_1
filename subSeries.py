# a program to print all sub series

# print the number
def pr(number,n):
    if number != 0 :
        print("{" , str(number).replace("", " ")[1: -1] , "}")
        if(number%10==n):
            pr(number//10,n)
        else:
            if len(str(number)) != 1:
                newnumber = newNum(number,n)
                pr(newnumber,n)
# to create new number
def newNum(number,n):
    s = 0
    j = n-number%10-1
    k = j
    for i in range(number%10+1,n+1):
        s += i*(10**j)
        j -= 1
    result = str(number//(10)) + str(s)
    return int(result)

# get the number
n = int(input())

# to create and see the result
for j in range(1 , n+1):
    a = ''
    for i in range(j,n+1):
        a += str(i)
    # print(a)
    pr(int(a),n)

# to print empety sub serie
print("{ }")