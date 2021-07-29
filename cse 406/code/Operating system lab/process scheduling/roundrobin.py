#Id : 17201026
import operator # for tuple sorting
n= int(input("number of process: ")) # taking input of how many jobs/ processes
q= int(input("Quantam: ")) # Quantam input

store= [] # to store all processes in python list

d={}# dictionary, for calculating wating time 

totalProcesTime=0
for i in range(n):
    process=input() # taking input of process name
    burst= int(input()) # taking input of process name
    totalProcesTime=totalProcesTime+burst
    d[process]=[] # {"p1":[],"p2":[],} for waiting time calculation, time count, initialize 
    store.append([process,burst]) # name, burst 2d array



indx=0
timeStamp=0
newAddingTime=0
strg="0 "


while (totalProcesTime > 0): #if total process time is not zero then run loop
     # total time minus quantam
    name=store[indx][0]
    if store[indx][1] !=0:
        d[name].append(timeStamp) #{"p1":[0,...], "p2":[5, ...],.. }
        if store[indx][1] >=q: # if the value is greater than quantam
            store[indx][1]=store[indx][1]-q # q for quantam
            timeStamp=timeStamp+q # q for quantam
            newAddingTime=q # q for quantam
            
        else: #if required process time is less than 5
            timeStamp=timeStamp+ store[indx][1] 
            newAddingTime= store[indx][1]
            store[indx][1]=0 

        d[name].append(timeStamp) #{"p1":[0,5,..], "p2":[5, ...],.. }

        strg = strg+" " + name +" "+ str(timeStamp)+" "

        totalProcesTime=totalProcesTime-newAddingTime


    indx=indx+1
    if indx == len(store):#round condition
        indx=0



print("RoundRobin Gantt chart: "+ strg)


#waiting time calculation
w=0
for k,i in d.items(): #d is dictionary i=[0,5,15,....] #k=process name
    
    w=w+i[0] #first value from list have to be calculated as wating time  
    i.pop(0) # now delete the first value, as it is calculated 

    for j in range(0,len(i),2):
        try:            
            w=w+i[j+1]-i[j]
        except:
            pass

w=w/len(store)
print("waiting time: "+ str(w))




