#Accesing elements in lists 
l = [1,2,3,"Gana"]
print(l[-1])

#Given two sets,find their intersection (common elements) and union(all unique elements combined)
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

uset = set1.union(set2)
iset = set1.intersection(set2)

print(uset,iset)