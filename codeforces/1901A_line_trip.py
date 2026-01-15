t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    gas_stations = list(map(int, input().split()))

    max_successive_diff = 0
    last_fuelled_at = 0
    for i in range(n):
        max_successive_diff = max(max_successive_diff, gas_stations[i] - last_fuelled_at)
        last_fuelled_at = gas_stations[i]
    
    max_successive_diff = max(max_successive_diff, (x - gas_stations[n-1]) * 2)
    print(max_successive_diff)