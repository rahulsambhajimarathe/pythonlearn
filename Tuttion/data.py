s = "babad"
n = len(s)


for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length

print(j)  # Output: "bab" or "aba"
