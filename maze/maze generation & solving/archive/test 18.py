L=[1,2,3]
M=[L[0],L[1]]
L[0]=7
print(M)
for i in range(1, 9):
    exec(f"a{i} = {i}")
    a1 = 1
    print(f"a{i}")


