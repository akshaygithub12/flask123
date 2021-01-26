a=input("enter the key")
x=input("enter my name")
y=input("asa")
d={"23":"asda","asdsd":"23","dfsf":"35","a":"akshay","ty":"akshahgasa",x:y}
print(d)
if a in d:
	del d[a]
else:
	print("key isnt found")
	exit(0)
print("updated dictionanry")
print(d)
	

