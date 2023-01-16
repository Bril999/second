"""Билет 24"""
string = input()
SUM = 0
string = string.split()
for nums in range(len(string)):
    string[nums] = int(string[nums])

string = sorted(string)
SUM = string[0] + string[1]
print(SUM)
