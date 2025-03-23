#Create dictnories,access values,update values,and iterable through key value pairs
my_dict = {
    "name" : "John",
    "age" : 30,
    "city" : "New york"
}
for i,j in my_dict.items():
    print(i,j)    
    

#Method - 2
my_dict = {}
name = input("Give Name: ")
age = int(input("Give age: "))
city = input("Give city name: ")


my_dict["name"] = name
my_dict["age"] = age
my_dict["city"] = city

print(my_dict)



