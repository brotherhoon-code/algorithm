from math import sqrt
from math import dist
import math

### 아래 코드는 greedy를 이용하여 틀린 문제입니다.


n_point, n_route = map(int, input().split())

points = []
connected = []
unconnected = []
answer = 0 # 리턴할 답


# 모든 포인트들을 points 리스트에 저장
for point in range(n_point):
    p_x, p_y = map(int, input().split())
    points.append((p_x,p_y))


# 연결된 포인트들을 connected 리스트에 저장
for route in range(n_route):
    src, dst = map(int, input().split()) 
    connected.append(src-1)
    connected.append(dst-1) # idx-1 오류 방지

# unconnected list
unconnected = [idx for idx, _ in enumerate(points) if idx not in connected]


# 들어온 포인트들의 거리를 계산해서 리턴하는 함수
def get_dist(src, dst) :
    return math.dist(points[src],points[dst])



while len(unconnected)!=0: # 연결되지 않은 포인트의 리스트가 empty까지 반복
    
    candidate_point = None
    min_dist = 9999999999999999999999999999
    for con_p in connected: # 모든 connected point와
        for unc_p in unconnected: # unconnected을 모두 순회하며
            dist = get_dist(unc_p, con_p) # 거리를 구함
            if dist < min_dist: # 가장 짧은 거리가 나오면 업데이트
                min_dist = dist
                candidate_point = unc_p
    
    answer += min_dist # 가장 짧은 거리를 더하고
    unconnected.remove(candidate_point) # 포인트를 연결 안된 리스트에서 빼고
    connected.append(candidate_point) # 포인트를 연결된 리스트에 추가

print(f'{answer:.2f}')