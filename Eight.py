test = int(input())
for a in range(test):
    i = input()
    for c in range(len(i)):
        if(i[c]=="a"):
            i = i[0:c] + "e" + i[c+1:(len(i))]
        if(i[c]=="e"):
            i = i[0:c] + "i" + i[c+1:(len(i))]
        if(i[c]=="i"):
            i = i[0:c] + "o" + i[c+1:(len(i))]
        if(i[c]=="o"):
            i = i[0:c] + "u" + i[c+1:(len(i))]
        if(i[c]=="u"):
            i = i[0:c] + "a" + i[c+1:(len(i))]
        if(i[c]=="A"):
            i = i[0:c] + "E" + i[c+1:(len(i))]
        if(i[c]=="E"):
            i = i[0:c] + "I" + i[c+1:(len(i))]
        if(i[c]=="I"):
            i = i[0:c] + "O" + i[c+1:(len(i))]
        if(i[c]=="O"):
            i = i[0:c] + "U" + i[c+1:(len(i))]
        if(i[c]=="U"):
            i = i[0:c] + "A" + i[c+1:(len(i))]
        elif(i[c].isalpha()):
            if(i[c]=="z"):
                i = i[0:c] + "b" + i[c+1:(len(i))]
            elif(i[c]=="Z"):
                i = i[0:c] + "B" + i[c+1:(len(i))]
            else:
                ch = (hex(i[c]) + 1)
                n = str(ch)
                print(n)
                #i = i[0:c] + (i[c]+1) + i[c+1:(len(i))]
    print(i)