#Remove duplicate elements from a list to create a new list with unique elements
#10,20,30,20,40,10,50
#inp = input("Give the values of lists:").split(",")

#l = [int(item) for item in inp]

#remove duplicate and create a new list

#NewL = []

#iterate over all the elements

#for i in l:
   # if i in NewL:
     #   continue
  #  else:
 #       NewL.append(i)
#print("Result:",NewL)


#process - 2
inp = input().split(",")

l = [int(a) for a in inp]

s = set(1)

NewL = list(s)

print(NewL)
