testCases = int(input())
for t in range(testCases):
    numSteps = int(input())
    numChamber = int(input())
    positions2 = input().split()
    dp = [0] * (int(numSteps)+1)
    curStep = 0

    positions = [0] * len(positions2)
    for t in range(len(positions2)):
        positions[t] = int(positions2[t])



    if(numChamber>0):
        for x in range(len(positions)):
            positions[x] = int(positions[x]) - 1



    if(0 not in positions):
        dp[0] = 1
    if(1 not in positions): 
        dp[1] = 1 + dp[0]
    curStep = 2

    #small cases

    while(curStep<numSteps):
        #print("n")
        # print(curStep)
        # print(positions)
        if(curStep in positions):
            # print("in")
            # print(curStep)
            dp[curStep] = 0
        else:
            dp[curStep] = dp[curStep-1] + dp[curStep-2]
        curStep+=1
    #print(dp)
    print(dp[numSteps-1])
        
        












# testCases = int(input())
# for t in range(testCases):
#     numSteps = int(input())
#     numChamber = int(input())
#     positions = input().split()
#     dp = [0] * (int(numSteps)+1)

#     if(0+1 not in positions):
#         dp[0] = 1
#     if(1+1 not in positions): 
#         dp[1] = 1 + dp[0]

#     if(numSteps<2):
#         print (dp[numSteps])
#     else:
#         for a in range(3,numSteps+1):
#             #print(dp)
#             nextDP = [0] * (numSteps+1)
#             for r in range(0,len(dp)):
#                 nextDP[r] = dp[r]
#             if(numChamber==0):
#                 nextDP[a] += (nextDP[a-2]+nextDP[a-1])
#             else:
#                 if((a-2+1) not in positions):
#                     nextDP[a] += nextDP[a-2]
#                 if((a-1+1) not in positions):
#                     nextDP[a] += nextDP[a-1]
#                 if((a+1) in positions):
#                     nextDP[a] = 0
#             #print(nextDP)
#             dp = nextDP
#         print(dp)
#         print(dp[numSteps])
                
