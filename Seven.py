i = input()

def reduce(s):
    li = [0] * len(s)
    subtract = False
    for a in i:
        if(a=="("):
            if(subtract):
                li[a] = int(li[a-1])
                subtract = False
            else:
                li[a] = int(li[a-1] + 1)
        if(a==")"):
            if(subtract):
                li[a] = int(li[a-1]) - 1
                subtract = False
            else:
                li[a] = int(li[a-1])
                subtract = True
    return "x"
                


while(i != "ALL YOU BASE ARE BELONG TO US"):
    good = True
    single = False
    if("(" not in i):
        if(len(i)==1):
            single = True
            print(i)
    if(not single):
        print(reduce(str(i)))
        




    i = input()

