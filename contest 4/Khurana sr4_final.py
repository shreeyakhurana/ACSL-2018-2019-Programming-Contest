
def addition(numb1, numb2):
    new = numb1 + numb2
    return new

def subtraction(numb1, numb2):
    new = numb1 - numb2
    return new

def multiplication(numb1, numb2):
    new = numb1 * numb2
    return new

def switch(a, b, c):
    if(a > 0):
        new = b
    else:
        new = c
    return new

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def solve(line):
    inputList = line.split(" ")
    while(len(inputList) > 1):
        indexI = 0
        while(indexI < len(inputList)):
            if(inputList[indexI] == '+' and is_number(inputList[indexI + 1]) and is_number(inputList[indexI + 2])):
                new = addition(int(inputList[indexI + 1]), int(inputList[indexI + 2]))
                del inputList[indexI : indexI + 3]
                inputList.insert(indexI, new)
                indexI = indexI + 1
            elif(inputList[indexI] == '-' and is_number(inputList[indexI + 1]) and is_number(inputList[indexI + 2])):
                new = subtraction(int(inputList[indexI + 1]), int(inputList[indexI + 2]))
                del inputList[indexI : indexI + 3]
                inputList.insert(indexI, new)
                indexI = indexI + 1
            elif(inputList[indexI] == '*' and is_number(inputList[indexI + 1]) and is_number(inputList[indexI + 2])):
                new =  multiplication(int(inputList[indexI + 1]), int(inputList[indexI + 2]))
                del inputList[indexI : indexI + 3]
                inputList.insert(indexI, new)
                indexI = indexI + 1
            elif(inputList[indexI] == '|' and is_number(inputList[indexI + 1])):
                new =  abs(int(inputList[indexI + 1]))
                del inputList[indexI: indexI + 2]
                inputList.insert(indexI, new)
                indexI = indexI + 1
            elif(inputList[indexI] == '@' and is_number(inputList[indexI + 1]) and is_number(inputList[indexI + 2]) and is_number(inputList[indexI + 3])):
                new =  switch(int(inputList[indexI + 1]), int(inputList[indexI + 2]), int(inputList[indexI + 3]))
                del inputList[indexI : indexI + 4]
                inputList.insert(indexI, new)
                indexI = indexI + 1
            elif(inputList[indexI] == '>' and is_number(inputList[indexI + 1]) and is_number(inputList[indexI + 2]) and is_number(inputList[indexI + 3])):
                new =  max(int(inputList[indexI + 1]), int(inputList[indexI + 2]), int(inputList[indexI + 3]))
                del inputList[indexI : indexI + 4]
                inputList.insert(indexI, new)
                indexI = indexI + 1
            else:
                indexI = indexI + 1
    print(inputList[0])



f = open("contest4_input.txt", "r")
count = 1
for line in f:
    print(str(count) + ". ")
    solve(line)
    count += 1

