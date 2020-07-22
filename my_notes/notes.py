# import time


# print('\n\n')
# start = time.time()


# def recursive(x):
#     if x == 0:
#         return x
#     return recursive(x-1)
#     print(x)


# x = 5        # 995
# print(x)
# x = recursive(x)
# # print(recursive(x))
# print(x)
# end = time.time()
# print(f'\nseconds = {end - start:.03f}\n')


def cd(n):
    if n == 0:
        return
    cd(n-1)
    print(n)
    cd(n-1)

cd(3)