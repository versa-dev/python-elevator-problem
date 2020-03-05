def solution(A, B, M, X, Y):
  weight = 0
  member = 0
  num = 1
  floor = ""
  index = 0
  b = B.split(",")
  for item in A.split(","):
    if((weight + int(item)) > Y or member == X):
      floor = ""
      weight = 0
      member = 0
      num += 1

    weight += int(item)
    member += 1

    if(floor.count(b[index]) == 0):
      floor += b[index]
      num += 1
    
    index += 1
    
  return num

A = input("Input the weights of the people: ")
B = input("Input the floors of the people: ")
M = input("Input the floor of apartment: ")
X = input("Input the capacity number of people: ")
Y = input("Input the capacity weight of elevator: ")

print(solution(A, B, int(M), int(X), int(Y)))