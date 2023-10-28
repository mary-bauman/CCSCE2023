n = int(input())
while n != 0:
    pts = {}
    win = False
    for i in range(n):
        l = input().split(" ")
        if l[1] == "GROUND": continue
        
        if l[0] == "JACKPOT" and not win:
            print("The winner is " + l[1] + ".")
            win = True
        elif l[0] == "BANKRUPT":
            pts[l[1]] = 0
        else:
            if not l[1] in pts:
                pts[l[1]] = 0
            pts[l[1]] += int(l[0])
            if pts[l[1]] >= 500 and not win:
                print("The winner is " + l[1] + ".")
                win = True

    if not win:
        print("There is no winner.")

    n = int(input())