# number = "645"
# temp = number 
# sum = 0
# for i in temp:
    
#     i = int(i)
#     sum = i[0]
#     print(i)

# def sum_digits(num):
num = 6586    
while num > 9:
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    num = digit_sum

    

print(num)
