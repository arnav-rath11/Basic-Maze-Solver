from copy import deepcopy 
from os import system

matrix=eval(input("Enter a NxN matrix (Use hashtags for wall and space for empty area): "))
lens=[] 
i=len(matrix)-1 
j=0
sols=[[[i,j]]] 
t=True 
SOLS=[]

while t:
    newSols=[]
    for i in range(0,len(sols)): 
        pos=sols[i][-1] 
        x=pos[0]
        y=pos[1] 
        try:
            path=deepcopy(sols[i])
            if matrix[x+1][y]==" " and [x+1,y] not in path: 
                x1,y1=x+1,y
                path.append([x1,y1]) 
                newSols.append(path)
            else:
                pass
            if x1==0 and y1==len(matrix[0])-1: 
                if path in SOLS:
                    pass
                else:
                    if path[-1]==[0,len(matrix[0])-1]: 
                        m=deepcopy(matrix)
                        for i in range(0,len(path)): 
                            m[path[i][0]][path[i][1]]=str(i)
                        for i in m:
                            print(i) 
                        print("XXXXXXXXXXXXXXX")
        except Exception as e: 
            pass
        try:
            path=deepcopy(sols[i])
            if matrix[x][y+1]==" " and [x,y+1] not in path: 
                x2,y2=x,y+1
                path.append([x2,y2]) 
                newSols.append(path)
            else:
                pass
            if x2==0 and y2==len(matrix[0])-1: 
                if path in SOLS:
                    pass
                else:
                    if path[-1]==[0,len(matrix[0])-1]: 
                        m=deepcopy(matrix)
                        for i in range(0,len(path)): 
                            m[path[i][0]][path[i][1]]=str(i)
                        for i in m:
                            print(i) 
                        print("XXXXXXXXXXXXXXX")
        except Exception as e: 
            pass
        try:
            path=deepcopy(sols[i]) 
            if x-1>=0:
                if matrix[x-1][y]==" " and [x-1,y] not in path: 
                    x3,y3=x-1,y
                    path.append([x3,y3]) 
                    newSols.append(path)
                else:
                    pass
                if x3==0 and y3==len(matrix[0])-1: 
                    if path in SOLS:
                        pass
                    else:
                        if path[-1]==[0,len(matrix[0])-1]: 
                            m=deepcopy(matrix)
                            for i in range(0,len(path)): 
                                m[path[i][0]][path[i][1]]=str(i)
                            for i in m:
                                print(i) 
                            print("XXXXXXXXXXXXXXX")
        except Exception as e: 
            pass
        try:
            path=deepcopy(sols[i]) 
            if y-1>=0:
                if matrix[x][y-1]==" " and [x,y-1] not in path: 
                    x4,y4=x,y-1
                    path.append([x4,y4]) 
                    newSols.append(path)
                else:
                    pass
                if x4==0 and y4==len(matrix[0])-1: 
                    if path in SOLS:
                        pass
                    else:
                        if path[-1]==[0,len(matrix[0])-1]: 
                            m=deepcopy(matrix)
                            for i in range(0,len(path)): 
                                m[path[i][0]][path[i][1]]=str(i)
                            for i in m:
                                print(i) 
                            print("XXXXXXXXXXXXXXX")
        except Exception as e: 
            pass
    lens.append(len(newSols)) 
    sols=newSols
    try:
        if sum(lens[-20:])/20==lens[-1]: 
            t=False
    except:
        pass 

system("PAUSE")