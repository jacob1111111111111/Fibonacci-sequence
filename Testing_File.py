# Fibonacci sequence
n_1 = 0
n_2 = 1
n_3 = 0
n = 1
print('F(1) = 1')

for i in range(100 - 1):
    n += 1
    n_3 = n_1 + n_2
    n_1 = n_2
    n_2 = n_3
    print(f'F({n}) = {n_3}')

# Prime numbers
# for i in range(2, 100):
#     for check in range(2, i):
#         if i % check == 0:
#             print(i)

