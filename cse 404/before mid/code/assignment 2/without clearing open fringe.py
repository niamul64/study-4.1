# id: 17201026
# python 3.8
# even Id, problem 2
import math
import heapq


def Gn(s,d):
    return math.sqrt((s[0]-d[0])**2+(s[1]-d[1])**2)
def Hn(s,d):#heuristic value
    return (abs(s[0]-d[0])+abs(s[1]-d[1]))


# main function
maze=[[  (0,0),(0,1),(0,2),      (0,4) ],# gap are the obstacles
        [(1,0),(1,1),(1,2),      (1,4) ],
        [(2,0),(2,1),(2,2),(2,3),(2,4) ],
        [(3,0),(3,1),(3,2),(3,3),(3,4) ],
        [(4,0),(4,1),(4,2),(4,3),(4,4) ],
        [(5,0),(5,1),(5,2),(5,3),(5,4) ]]

visit=[[0,0,0,None,0],
       [0,0,0,None,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       ]
       # 0 means not visited # 1 means vissited # none means can't visit 
        

goal=maze[5][4]
start=maze[0][0]
# Here , (5,4) is the Goal state
# start from (0,0)

close_fringe=[] #store current states
Open_fringe=[]# Priority queue
store={} #detail storing




#initializing the close_fringe
hn=Hn(start,goal)#heuristic value calculation call
fn=hn+0 # at starting gn=0

close_fringe.clear()

close_fringe.append(maze[0][0]) # fn,Gn,Hn
store[maze[0][0]]=[fn,0,hn]
# open_fringe empty now
visit[0][0]=1 #1 means visited
print("At first initialize the close fringe with start state: ",close_fringe[0])
print("f(n) of {} is : {:.2f} = {:.2f} + {:.2f}".format(start,fn,0,hn) )    




#calculate the neighbors for each value of closed fringe
nihbr=[]
x_bound=5
y_bound=4


for i in close_fringe:

  x,y=i
  nihbr.clear()
  nx=x-1
  ny=y

#collecting all possible neighbors which till not visited 
  if nx>=0 and visit[nx][ny] != None and visit[nx][ny] ==0:
    nihbr.append(maze[nx][ny])
    visit[nx][ny]=1
    
  
  nx=x-1
  ny=y+1
  if nx>=0 and ny<=y_bound and visit[nx][ny] != None and visit[nx][ny] ==0:
    nihbr.append(maze[nx][ny])
    visit[nx][ny]=1

  nx=x
  ny=y+1

  if nx >=0 and ny<=y_bound and visit[nx][ny] != None and visit[nx][ny] ==0:
    nihbr.append(maze[nx][ny])
    visit[nx][ny]=1



  nx=x+1
  ny=y+1
  if nx<=x_bound and nx>=0 and ny<=y_bound and visit[nx][ny] != None and visit[nx][ny] ==0:
    nihbr.append(maze[nx][ny])
    visit[nx][ny]=1
  
  nx=x+1
  ny=y
  if nx<=x_bound and nx>=0 and ny<=y_bound and visit[nx][ny] != None and visit[nx][ny] ==0:
    nihbr.append(maze[nx][ny])
    visit[nx][ny]=1

  nx=x+1
  ny=y-1
  if nx<=x_bound and ny>=0 and nx>=0 and ny<=y_bound and visit[nx][ny] != None and visit[nx][ny] ==0:
    nihbr.append(maze[nx][ny])
    visit[nx][ny]=1
  nx=x
  ny=y-1
  if nx<=x_bound and ny>=0 and nx>=0 and ny<=y_bound and visit[nx][ny] != None and visit[nx][ny] ==0:
    nihbr.append(maze[nx][ny])
    visit[nx][ny]=1

  nx=x-1
  ny=y-1
  if nx<=x_bound and ny>=0 and nx>=0 and ny<=y_bound and visit[nx][ny] != None and visit[nx][ny] ==0:
    nihbr.append(maze[nx][ny])
    visit[nx][ny]=1
#collecting all possible neighbors which till not visited (end)
  
  fn,gn,hn=store[i] # details of current state
  if len(nihbr)>0:
    print("neighbors of",i,'are',nihbr)
    for j in nihbr:
      print("cost needed form {} to {} : {:.2f}".format(i,j,Gn(i,j))) # distanse form current state to neighbor state
      ngn=Gn(i,j)+gn
      nhn=Hn(j,goal)
      nfn=ngn+nhn
      print("f(n) of",j,'is',"{:.2f}".format(nfn),'=',"{:.2f}".format(ngn),'+',"{:.2f}".format(nhn))
      store[j]= [nfn,ngn,nhn]
      Open_fringe.append((store[j],j))
      
    print('\n')# two line gap
    heapq.heapify(Open_fringe)
    sd,sn=Open_fringe[0] # sn = (x,y) of next selected node which has lowest f(n) # sd=selected neighbor's fn,gn,hn 
    heapq.heappop(Open_fringe)
    print('now, the current position is', sn)
    close_fringe.append(sn)


print("Now, we reached to goal", i)
gfn,ggn,ghn=sd # sd=selected neighbor's fn,gn,hn 
print("f(n) of {} is : {:.2f} = {:.2f} + {:.2f}".format(i,gfn,ggn,ghn) )


#effective path to reach the final state
print("\n\nNow, the cost effective path to reach the final state from initial state is: ")
totalCost=0
for i in close_fringe:
  fn,gn,hn=store[i]
  if gn>0:
    print("--> ","{:.2f}".format(gn),"-->",end=" ")
  totalCost= totalCost+gn
  print(i,end=" ")
print("")#line gap

print("Total cost: ","{:.2f}".format(gn))

