#2차원 맵을 잘 정의할 것
# 둘러쌓인 부분을 어떻게 정의하는가? : 4개의 코너에서 BFS를 수행하면 됨
#visited가 다 1이 되면, 종료할것임.
#visited가 1인 것은, 이미 방문했다는 것.
#visitied가 2인 것은, 방문은 안했어도 알 수는 없다는 것임.
#grid_map은 이 지형의 정보를 저장함.
from collections import deque
SIZE=10
grid_map=[[0 for _ in range (SIZE+2)] for _ in range (SIZE+2)]
visited=[[0 for _ in range (SIZE+2)] for _ in range (SIZE+2)]

class Robot:
    def __init__(self,num,x,y,dx,dy):
        self.num=num
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy  # head가 향하는 방향

    #아래는 현재 향하는 머리 방향으로부터의 앞/뒤/왼쪽/오른쪽 이동임
    def move_front(): #전진

    def turn_right(): #우회전

    def turn_left(): #좌회전 

    def move_back(): # 후진

    def move_left(): #좌회전 후 전진

    def move_left(): #우회전 후 전진
    
    
    def get_method(target_x, target_y):



def is_out(a,b):
    if a==0 or a==SIZE+1 or b==0 or b==SIZE+1:
        return False
    else: return True

def renew_surrounded():
    tmp_visited=[[2 for _ in range (SIZE+2)] for _ in range (SIZE+2)]
    queue=deque()
    queue.append((1,1))
    queue.append((10,10))
    while queue:
        p,q=queue.popleft()
        tmp_visited[p][q]=0
        for dp, dq in [(-1,0),(0,1),(1,0),(0,-1)]:
            np,nq=p+dp,q+dq
            if is_out(np,nq) and grid_map(np,nq)==1:
                tmp_visited[np][nq]=1
            elif is_out(np,nq) and grid_map(np,nq)==0 and tmp_visited[np][nq]==2:
                queue.append(np,nq)
                tmp_visited[np][nq]=0
    global grid_map
    grid_map=tmp_visited


def BFS(a,b,x,y): #from(a,b) to (x,y)
    tmp_visited=[[0 for _ in range (SIZE+2)] for _ in range (SIZE+2)]
    queue=deque()
    queue.append((a,b))
    visited[a][b]=1
    while queue:
        p,q=queue.popleft()
        tmp_visited[p][q]=1
        if (p,q)==(x,y): return True
        for dp, dq in [(-1,0),(0,1),(1,0),(0,-1)]:
            np,nq=p+dp,q+dq
            if is_out(np,nq) and grid_map[np][nq]==0:
                queue.append(np,nq)
                visited[np][nq]=1



def nextcoord(p,q):
    for dp, dq in [(-1,0),(0,1),(1,0),(0,-1)]:
            np,nq=p+dp,q+dq
            if is_out(np,nq) and grid_map[np][nq]==0 and visited[np][nq]==0:
                return (np,nq)
    for dp, dq in [(-1,0),(0,1),(1,0),(0,-1)]:
            np,nq=p+dp,q+dq
            if is_out(np,nq) and grid_map[np][nq]==0:
                return (np,nq)


