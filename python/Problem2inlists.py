#FIND THE MAXIMUM AND MINIMUM VALUES IN A LIST OF A NUMBERS
#Proccess - 1
#l = [15,2,7,25,10]

#maxi = l[0]
#mini = l[0]
#for i in l:
 #   if i > maxi:
  #      maxi = i
   # if i < mini:
    #    mini = i
        
#print("Maximum = ",maxi,";Mini = ",mini,sep="")

#Process - 2
l = [15,2,7,25,10]

l.sort() 

print("Maximum = ",l[-1],";Minimum = ",l[0],sep="")



