t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    sorted_a = sorted(a)
    
    if sorted_a == a or k > 1:
        print("YES")
    else:
        print("NO")


