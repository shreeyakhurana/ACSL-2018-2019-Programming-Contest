#Senior 2018-19
#Contest 1
#Digit Reassembly

def solve(input1):
    inputlist = input1.split(" ")
    numbInt = int(inputlist[0])
    numbStr = inputlist[0]
    length = int(inputlist[1])
    if(len(numbStr) % length == 0):
        summing(numbStr, length)
    else:
        newNumbStr = addZeros(numbStr, length)
        summing(newNumbStr, length)


def summing(numbStr, length):
    seperate = [numbStr[i:i+length] for i in range(0, len(numbStr), length)]
    total = 0
    for x in seperate:
        total = total + int(x)
    print(total)


def addZeros(numbStr, length):
    while(len(numbStr)% length != 0):
        numbStr = numbStr + '0'
    return numbStr


f = open("contest1_input.txt", "r")
count = 1
for line in f:
    print(str(count) + ". ")
    solve(line)
    count += 1
