print("Enter the no. of processes")
process = []
N = int(input())
for _ in range(N):
    status = int(input())
    process.append(status)
print(process)
process[N - 1] = 0
print(process)
print("process" + str(N) + "has failed")
print("Enter process which initiates election")
initiator = int(input())
alive = []
for _ in range(initiator + 1,N):
    if(process[_ - 1] == 1):
        print(str(_) + " answers to inquiry of " + str(initiator))
        alive.append(_)
if not alive:
    print(str(initiator) + " is final co-ordinator")
else:
    print("yeah")



def bully_election(initiator):
    for _ in range(N):
        if(process[i] > process[initiator])
        
    
