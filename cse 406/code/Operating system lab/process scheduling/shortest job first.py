#Id : 17201026
import operator # for tuple sorting
n= int(input("number of process: ")) # taking input of how many jobs/ processes

store= {} # to store all processes in python dictonary/ hash


for i in range(n):
    process=input() # taking input of process name
    burst= int(input()) # storing to dictonary {'process':burst, 'process':burst,}

    store[process]=burst
    
sort = dict( sorted(store.items(), key=operator.itemgetter(1)))# tuple sorting, converting to dictonary

store=sort # again storing to previous variable


w=0
for i,j in store.items():
    w=w+j
    store[i]=w # storing waiting for next process


strg="0 "
Waiting=0
for i,j in store.items():
    Waiting=Waiting+j # sum of all waitings
    strg = strg+" " + i +" "+ str(j)+" "

Waiting=(Waiting-j)/len(store)# waiting calculating variable
print("the waiting time: "+str(Waiting))

print("the gantt chart: "+strg)





