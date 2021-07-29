#Id : 17201026
#input 98 183 37 122 14 124 65 67

def close(target,array):
    if len(array)==1:
        return array[0]
    dis=abs(target-array[0])
    cloest=array[0]
    for i in array:
        if abs(target-i)<dis:
            dis=abs(target -i)
            cloest=i
    return cloest




InputQueue= input("Enter the queue: ").split(" ") # taking queue input
head= int(input("Enter Head start at: "))
print()#line gap

queue = [int(value) for value in InputQueue]


pre=head

path=[]
path.append(head)

while len(queue)!=0:
    closest=close(pre,queue)
    path.append(closest)
    queue.remove(closest)
    pre=closest

print("path: ", path)
    
#distance calculate
pre=head
totalDistance=""
distance=0
for i in path: # first value of path is head
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