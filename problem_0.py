# def fibonacci(n:int)->list[int]:
#     a = 0
#     b = 1
#     arr = []
#     for i in range(n):
#         a, b = b, a+b # 1, 1
#         arr.append(a)
    
#     return arr

def sum_square_nums(n:int)->int:
    result = 0
    
    for i in range(1, n+1):
        if i%2==0:
            continue
        else:
            result += i**2
            # print(i, result)

    return result

print(sum_square_nums(588000))

