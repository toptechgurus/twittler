
s = input('enter the roman number')
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
temp = 0
for i in range(len(s)):
    if i > 0 and roman[s[i]] > roman[s[i - 1]]:
        temp += roman[s[i]] - 2 * roman[s[i - 1]]
    else:
        temp += roman[s[i]]

print('the integer value is', temp)