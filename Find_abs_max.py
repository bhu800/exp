#given an input from the user as space seperated numbers it will output the maximum abs. value:-

arr = list(map(int,input().split())
for i in arr:
  if i<0:
    i=-1*i
print(max(arr))
