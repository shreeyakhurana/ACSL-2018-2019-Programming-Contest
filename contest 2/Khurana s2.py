
def diff(string1, string2):
    list1 = string1.split()
    common = ""
    for word in list1:
        if(string2.find(word) >= 0):
            common = common + " " + word
            string2 = string2.replace(word, "", 1)
    common = common.lstrip()
    return common

def secondAlg(com1, com2):
    com2List = []
    common = ""
    for c in com2:
        if(c != ' '):
            com2List.append(c)
    for i in range(len(com1)):
        if com1[i] in com2List:
            common = common + com1[i]

            index = com2List.index(com1[i])
            for k in range(index+1):
                com2List.pop(0)
    if(common == ""):
        common = "NONE"

    return common

f = open("contest2_input.txt", "r")
count = 1
while True:
    line1 = f.readline()
    line2 = f.readline()
    if not line2: break
    print(str(count) + ". ")
    com1 = diff(line1, line2)
    com2 = diff(line2, line1)
    print(secondAlg(com1, com2))
    count += 1
