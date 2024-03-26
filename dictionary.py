mp = {}

v = [1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7, 7, 8, 9, 9, 9]

for num in v:
    if num in mp:
        mp[num] += 1
    else:
        mp[num] = 1

for key, value in mp.items():
    print(key, value)
