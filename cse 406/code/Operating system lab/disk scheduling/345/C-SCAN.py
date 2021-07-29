#Id : 17201026
#input 98 183 37 122 14 124 65 67

def splitQueue(head,array):
    lower=[]
    upper=[]
    for i in array:
        if i < head :
            lower.append(i)
        else:
            upper.append(i)
    upper.sort()
    lower.sort()
    

    return (lower,upper)


InputQueue= input("Enter the queue: ").split(" ") # taking queue input
head= int(input("Enter Head start at: "))
LB= int(input("Enter lower bound: ")) #lower bound
UB= int(input("Enter upper bound: ")) #upper bound

print()#line gap

queue = [int(value) for value in InputQueue] 
L,U=splitQueue(head,queue)#  [] []

#path
U.insert(0,head) #start from head , '0' first index
if UB != U[len(U)-1]: # if upper bound not toched
    U.append(UB) # UB= upper bound

if L[0]!=LB: # LB= lower bound , L =lower array
    L.insert(0,LB) # '0' first index , goto Lower Bound
U.extend(L) # adding lower array


print("path: ", U)



    
#distance calculate
pre=head
totalDistance=""
distance=0
for i in U: # first value of path is head
    if i==head:
        continue
    if pre>int(i):
        totalDistance= totalDistance+'('+str(pre)+'-'+str(i)+')+'
        distance= distance + pre - i
    else:
        totalDistance= totalDistance+'('+str(i)+'-'+str(pre)+')+'
        distance= distance + i - pre
    pre=i

print()

print("Total distance: "+totalDistance[0:len(totalDistance)-1]) 
print('Illustration shows total head movement of = '+str(distance))