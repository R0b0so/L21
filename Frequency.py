test_dict = {"A": 2, "B": 2, "C": 2, "D": 2, "E": 1, "F": 2,}
print("Original Dictionary:" + str(test_dict))
G = 2
res = 0
for key in test_dict:
    if test_dict[key] == G:
        res = res + 1
print("The amount of 2s in the string are:", res)