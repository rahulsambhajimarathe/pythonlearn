# list1 = [[65, 6, 6], [26, 89, 91], [45, 20, 3]]
# list2 = [[20, 6, 7], [8, 6, 9], [3, 2, 1]]

# # a = len(list1) == len(list2)
# # print(a)
# # a = len(list1)
# # if len(list1) == len(list2):
# i = 0
# while i in len(list2):
#     b = 0
#     while b in len(list2):
#         print(list2[i][b])
#         b += 1
#     i += 1
    
list1 = [[65, 6, 6], [26, 89, 91], [45, 20, 3]]
list2 = [[20, 6, 7], [8, 6, 9], [3, 2, 1]]

sum_by_index = []

for i in range(len(list1[0])):
    total = 0
    for sublist in list1 + list2:
        total += sublist[i]
    sum_by_index.append([total])

print(sum_by_index)


