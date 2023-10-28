t = input()
for a in range(int(t)):
    text = str(input())
    place = str(input())
    sequence = input().split(" ")
    #print(sequence)
    for b in sequence:
        if(b!=''):
            s = ""
            t = 0
            while(t<len(text)):
                if(text[t:(t + len(place))]== place):
                    #print("place")
                    s+=b
                    t = t + len(place)
                else:
                    s = s + text[t]
                    t+=1
            # if(text[t:len(text)]== place):
            #         #print("place")
            #         s+=b
            #         t = t + len(place) 
            # if(text[(len(text)-1)]==place):
            #     s+=b
            print(s)


    
    # for x in sequence:
    #     s = ""
    #     curPlace = 0
    #     c = 0
    #     while(c<len(text)):
    #         if(text[c]==place[curPlace]):
    #             curPlace +=1
    #             if(curPlace == len(x)):
    #                 s += x
    #             print("if stmt " + s)
    #         else:
    #             s+=text[c]
    #             curPlace = 0
    #         c+=1
    #         print("curS = " + s)
    #     print(s)



