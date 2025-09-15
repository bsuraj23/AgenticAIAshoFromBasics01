d = {'fruits': ['apple', 'banana']}
d2 = {'marks': [85, 90, 95]}
d3 = {'letters': list('abc')}
d4 = {'nums': list(range(5))}
d5 = {'data': [1.1, 2.2, 3.3]}
print(d)
print(d2)
print(d3)
print(d4)
print(d5)

d5.clear()

a=90
print(type(a))
print(d5)



#Iterations examples
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

#TODO: Add more examples for dict with list different Data types values and their manipulations
