d = {'coords': (10, 20)}
d2 = {'rgb': (255, 255, 0)}
d3 = {'version': (3, 8)}
d4 = {'date': (2025, 7, 10)}
d5 = {'grades': ('A', 'B', 'C')}

print(d)
print(d2)

print(d3)
print(d4)
print(d5)

#iteraites examples
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")
for key, value in d2.items():
    print(f"Key: {key}, Value: {value}")
for key, value in d3.items():
    print(f"Key: {key}, Value: {value}")
for key, value in d4.items():
    print(f"Key: {key}, Value: {value}")
for key, value in d5.items():
    print(f"Key: {key}, Value: {value}")
