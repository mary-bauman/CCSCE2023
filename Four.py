n = int(input())

while n != 0:
    stk = []
    loc = [0,0]
    dir = 0
    prog = [input().split(" ") for _ in range(n)]
    
    i = int(0)
    while (i < int(len(prog))):
        l = prog[i]
        if l[0] == "push":
            stk.append(int(l[1]))
        elif l[0] == "add":
            stk.append(stk.pop() + stk.pop())
        elif l[0] == "move":
            dist = stk.pop()
            if dir % 4 == 0:
                loc[1] += dist
            elif dir % 4 == 1:
                loc[0] -= dist
            elif dir % 4 == 2:
                loc[1] -= dist
            elif dir % 4 == 3:
                loc[0] += dist
        elif l[0] == "turn":
            dir += stk.pop() / 90
        elif l[0] == "branch":
            if stk[-1] != 0:
                i = int(l[1])
                continue
        elif l[0] == "halt":
            break
        i+=1
    
    print("Mower halts at (" + str(loc[0]) + ", " + str(loc[1]) + ").")
    n = int(input())