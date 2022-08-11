import time

#Palindrome Iterative Solution
def pal(str):
  half = int(len(str)/2)
  for i in range(half):
    if str[i] != str[(len(str)-i)-1]:
      return False
  return True

#TestCases
s = time.time()
n = 'mom'
print('Input:', n)
print('Iterative Output:',pal(n))
e = time.time()
t = e - s
print('Runtime:', t, '\n')

s = time.time()
n = 'abba'
print('Input:', n)
print('Iterative Output:',pal(n))
e = time.time()
t = e - s
print('Runtime:', t, '\n')

s = time.time()
n = '0'
print('Input:', n)
print('Iterative Output:',pal(n))
e = time.time()
t = e - s
print('Runtime:', t, '\n')

#Palindrom Recursion Solution
def pal_r(word):
  l = len(word)
 #debugging print(word)

  if l == 0 or l == 1:
    return True
  
  elif word[0] != word[l-1]:
      return False
  return pal_r(word[1:l-1])#Recursive Step

#TestCases
s = time.time()
n = 'mom'
print('Input:', n)
print('Recursive Output:',pal_r(n))
e = time.time()
t = e - s
print('Runtime:', t, '\n')

s = time.time()
n = 'abba'
print('Input:', n)
print('Recursive Output:',pal_r(n))
e = time.time()
t = e - s
print('Runtime:', t, '\n')

s = time.time()
n = '0'
print('Input:', n)
print('Recursive Output:',pal_r(n))
e = time.time()
t = e - s
print('Runtime:', t, '\n')