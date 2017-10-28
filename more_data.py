arr = [4,6,8]
arr = arr + [10]
print(arr)

arr = arr + list('abc')
print(arr)

arr = arr + list(str(123))
print(arr)

arr.append([12,14,16])
print(arr)

arr.append(18)
print(arr)

arr.insert(1, 24)
print(arr)

arr.remove(4)
print(arr)