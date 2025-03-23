#Methods in lists 
#1)append():Adds an element to the end of the list
l = [1,2,3,4]
l.append(5)
print(l)
#2)insert():inserts an element at a specific index 
m = [1,2,3,4]
m.insert(0,5)
print(m)
#3)remove():Removes the first occurence of a specified element
n = [1,2,3,4]
n.remove(1)
print(n)
#4)pop():Removes and returns the element at a specified index
o = [1,2,3,4]
o.pop(0)
print(o)
#5)index():Returns the index of the first occurence of a specified element
p = [1,2,3,4]
print(p.index(4))
#6)count:Returns the number of occurences of a specified element in the list
q = [1,2,3,2,2,1,5,6,2,2]
print(q.count(2))
#7)sort():sorts the list in ascending order
r = [54,62,12,10]
r.sort()
print(r)
#8)reverse():Reverse the order of element in the list
s = [5,4,3,2,1]
s.reverse()
print(s)
