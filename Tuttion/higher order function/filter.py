# prime number
# for x in range(3, 100):
#     prime = True
#     for i in range(2, x):
#         if x%i==0:
#             prime = False
#         break
#     if prime:
#         print(x, "is a prime number")
        
        
# def prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# upper = int(input("Enter the prime list: "))

# number = filter(prime, range(3, upper + 1))

# print("Prime numbers between 3 and", upper, ":", list(number))

# lamda
# def prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# lim = int(input("Enter the prime list: "))

# pri = filter(lambda x: prime(x), range(3, lim + 1))

# print("Prime numbers between 3 and", lim, ":", list(pri))


# plaindrome

num = int(input("Enter an integer: "))

num_str = str(num)

palindrome = num_str + num_str[::-1]

palindrome_int = int(palindrome)

print(f"The palindrome is: {palindrome_int}")
