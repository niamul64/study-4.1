# id: 17201026
# python 3.8
# even Id, problem 2
import math
import heapq

nodeName=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
# main function


########################### input start
pathCost={(a,b):2,
          (a,c):3,
          (b,e):1,
          (c,e):2,
          (b,f):1,
          (e,g):9,
          (f,g):9

            }
Gn={}
heuristic={a:6,
           b:8,
           c:3,
           e:3,
           f:4
           
            }

path={}
goal=g  # set the goal node
start=a # set the start node
Gn[start]=0 # set the start node's gn whis is zero
heuristic[goal]=0 # goal node's hurestic value is zero
path[start]=(0,None,a)# (cost,pre,goal) # initialize with satrt node , no pre node for start node so None, and in between cost is zero 

#################  input ends here



close_fringe=[] #store current states
Open_fringe=[]# Priority queue
store={} #detail storing


close_fringe.append(start) 




for Citem in close_fringe:

    for nodes,cost in pathCost.items():
        current,nei=nodes

        if (current==Citem):
            try:
                cost_between=pathCost[(Citem,nei)]
                try:
                    
                    gn=cost_between+Gn[Citem] # gn[Citem] is the path cost of till previous node
                    
                    if Gn[nei]>gn:
                        Gn[nei]=gn
                        fn=gn+heuristic[nei]
                        Open_fringe.append((fn,nei))
                       

                except:
                    
                    cost_between=pathCost[(Citem,nei)]
                    gn=cost_between+Gn[Citem] # gn[Citem] is the path cost of till previous node
                    fn=gn+heuristic[nei]
                    Open_fringe.append((fn,nei))
                    Gn[nei]=gn

            except:
                pass
        # elif (nei==Citem):
        #     try:
        #         cost_between=pathCost[(Citem,current)]
        #         try:
                    
        #             gn=cost_between+Gn[Citem] # gn[Citem] is the path cost of till previous node
                    
        #             if Gn[current]>gn:
        #                 Gn[current]=gn

        #                 fn=gn+heuristic[current]
        #                 Open_fringe.append((fn,current))
   
        #         except:
                    
        #             cost_between=pathCost[(Citem,current)]
        #             gn=cost_between+Gn[Citem]# gn[Citem] is the path cost of till previous node
        #             fn=gn+heuristic[current]
        #             Open_fringe.append((fn,current))
        #             Gn[current]=gn
             
        #     except:
        #         pass

    heapq.heapify(Open_fringe)
    print('open fringe(fn,node)  ',Open_fringe)
    fn,selected_node=Open_fringe[0] 
    heapq.heappop(Open_fringe)
    close_fringe.append(selected_node)


    path[selected_node]=(pathCost[(Citem,nei)],Citem,selected_node)
    nod=(cost_between,Citem,selected_node)

    print('close fringe:         ',close_fringe)
    print(path)

    if selected_node==goal:
        print(selected_node)
        break
#initializing the close_fringe
# cost,pre,goal=nod
# while pre!=None:
#     print(goal,"<--",cost,'<--',pre,end=" ")
#     cost,pre,goal=path[pre]
#     if pre==None:
#         break
