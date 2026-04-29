test_dict = {'I' : 2, 'am' : 2, 'good' : 2, 'at' : 2, 'boxing' : 1} 

print("The original dictionary : " + str(test_dict))

k = 2

res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1

print("Frequency of k is :" + str(res))        