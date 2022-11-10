## calculate distance func
def get_dist(src, dst):
    return((src[0] - dst[0])**2 + (src[1] - dst[1])**2)**(1/2)

## find parent value func
def get_parent(node): 
    if union_table[node] == node:
        return node
    else:
        union_table[node] = get_parent(union_table[node]) # recursive
    return union_table[node]

## union check func
def is_union(p1, p2): 
    p1_parent = get_parent(p1)
    p2_parent = get_parent(p2)
    if p1_parent == p2_parent:
        return True # Union
    else:
        return False # not union


## make union func ★★★★★★★
def make_union(p1, p2): ## issue occur block
    p1_v = get_parent(p1)
    p2_v = get_parent(p2)
    union_table[max(p1_v, p2_v)] = min(p1_v, p2_v)


### start
num_p, num_r = list(map(int, input().split()))

list_pos = []
graph = [] # full graph
union_table = [i for i in range(num_p)] # union_table
answer = 0

for i in range(num_p):
    x, y = map(int, input().split())
    list_pos.append((x, y))

for j in range(num_r):
    p1, p2 = map(int, input().split())
    p1 = p1-1
    p2 = p2-1
    ## make union
    make_union(p1, p2)


## make dist table for all points
for idx1 in range(num_p-1):
    for idx2 in range(idx1+1, num_p):
        graph.append((idx1, idx2, get_dist(list_pos[idx1],list_pos[idx2])))


## sorting by distance
graph.sort(key=lambda x:x[2]) 

## iter all graph
for item in graph:
    p1, p2, dist = item
    if is_union(p1, p2): # if unioned pass
        continue
    else: # else not unioned
        # make union
        make_union(p1, p2)
        # input connected list
        answer+=dist

print(f"{round(answer,2):.2f}")