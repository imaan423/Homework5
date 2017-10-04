##Name: Imaan Munir

import re
filename = open('regex_sum_37794.txt')
list1 = []
for number in filename:
    find = re.findall('[0-9]+',number)
    list1.extend(find)


total = [int(i) for i in list1]
final = sum(total)
print (final)


