#Id : 17201026
import operator # for tuple sorting
n= int(input("number of process: ")) # taking input of how many jobs/ processes

store= [] # to store all processes in python list


for i in range(n):
    process=input() # taking input of process name
    burst= int(input()) # taking input of burst time
    priority= int(input()) # taking input of priority
    store.append((priority,process,burst)) #saving as tuple[(2,p1,21),(1,p2,3),......]
   
sort = sorted(store)# tuple sorting

store=sort # again storing to previous variable



time=[]
w=0
strg="0 "
for i,j,k in store:
    w=(k+w)
    time.append(w) # storing waiting for next process
    strg = strg+" " + j +" "+ str(w)+" "
w=0
for i in time:
   w=w+i
Waitng=(w-i)/len (time)
print('avarage waiting time: '+str(Waitng)) 


print("the gantt chart: "+strg)





