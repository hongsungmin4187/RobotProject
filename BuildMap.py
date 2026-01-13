#2차원 맵을 잘 정의할 것
# 둘러쌓인 부분을 어떻게 정의하는가? : 4개의 코너에서 BFS를 수행하면 됨
#visited가 다 1이 되면, 종료할것임.
#visited가 1인 것은, 이미 방문했다는 것.
#visitied가 2인 것은, 방문은 안했어도 알 수는 없다는 것임.
#grid_map은 이 지형의 정보를 저장함.



SIZE=10
grid_map=[[0 for _ in range (SIZE+2)] for _ in range (SIZE+2)]
visited=[[0 for _ in range (SIZE+2)] for _ in range (SIZE+2)]
class Robot_1:
    def get_ne




