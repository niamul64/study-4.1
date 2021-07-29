#Id : 17201026
n= int(input("number of process: ")) # taking input of how many jobs/ processes

store= {} # to store all processes in python dictonary/ hash

w=0 
for i in range(n):
    process=input() # taking input of process name
    burst= int(input()) # taking input of burst time
    w=w+burst 
    store[process]=w # storing to dictonary {'process':w, 'process':w,}
    

strg="0 " 
Waiting=0 # waiting calculating variable
for i,j in store.items():
    Waiting=Waiting+j  # sum of all waitings
    strg = strg+" " + i +" "+ str(j)+" "

Waiting=(Waiting-j)/len(store) # waiting calculating variable
print("the waiting time: "+str(Waiting))

print("the gantt chart: "+strg)





