#Id : 17201026
#input 98 183 37 122 14 124 65 67

queue= input("Enter the queue: ").split(" ") # taking queue input
head= int(input("Enter Head start at: "))
print()#line gap

pre=head
totalDistance=""
distance=0
print("Path: " + str(head) ,end=" ")
for i in queue:
    print(i,end=" ")
    if pre>int(i):
        totalDistance= totalDistance+'('+str(pre)+'-'+i+')+'
        distance= distance+pre-int(i)
    else:
        totalDistance= totalDistance+'('+i+'-'+str(pre)+')+'
        distance= distance+int(i)-pre
    pre=int(i) 
print()

print("Total distance: "+totalDistance[0:len(totalDistance)-1]) 
print('Illustration shows total head movement of = '+str(distance))
