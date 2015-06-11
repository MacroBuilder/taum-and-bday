def bw_cost(q1,q2,c1,c2,t):
    if c1 + t < c2:
        c2 = c1 + t
    elif c2 + t < c1:
        c1 = c2 + t
    return q1*c1 + q2*c2

test_cases = int(raw_input().strip())

for _ in range(test_cases):
    b, w = (int(i) for i in raw_input().strip().split())
    x, y, z = (int(i) for i in raw_input().strip().split())
    print bw_cost(b,w,x,y,z)
