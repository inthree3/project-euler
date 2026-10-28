# 9*91 = 81+9 = 819*11 = 8190+819 = 9009

# 111*9 

# 999999
# 998899
# 997799
# 996699
# 990099
# 989989

def has_two_3_digit_factors(n:int)->bool:
    for i in range(100, 1000):
        if n%i==0 and n//i<1000: return True
    return False

# print(has_two_3_digit_factors(999999))

def generate_pendulum(n:int)->int:
    digit = 0
    result = 0
    while True:
        digit += 1
        # print(n, 10**digit, n<10**digit)
        if n>=10**digit:
            continue
        else:
            break
    # print(digit)

    for i in range(1, digit+1):
        result += (n%10)*10**(digit+i-1) + (n%10)*10**(digit-i)
        n //= 10
        # print(n, result)
    return result

# print(generate_pendulum(839))

for i in range(999, 99, -1):
    pendulum = generate_pendulum(i)
    if has_two_3_digit_factors(pendulum):
        print(pendulum)
        break
