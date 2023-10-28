n = int(input())
for _ in range(n):
    first = ""
    last = ""
    win = False
    rms = {}
    child = {}

    nr = int(input())
    if nr == 0:
        print("There is no escape!")
        break
    for _ in range(nr):
        l = input().split(" ")
        if first == "": first = l[0]
        rms[l[0]] = int(l[1])
        last = l[0]
    
    nc = int(input())
    if nc == 0:
        print("There is no escape!")
        break
    for _ in range(nc):
        l = input()
        if l[0] not in child:
            child[l[0]] = []
        child[l[0]].append(l[1])
    
    stk = [first]
    while len(stk) > 0:
        cur = stk.pop()
        if last in child[cur[-1]]:
            if rms[last] >= len(cur) + 1:
                print("Montana can escape: "+cur+last)
                win = True
            break
        else:
            for c in child[cur[-1]]:
                if rms[c] >= len(cur)+1:
                    stk.append(cur+c)
    
    if not win:
        print("There is no escape!")