month={"dr":"dadar","b":"badra","pr":"parel"}
print(month)
for key in month:
	print key
a=raw_input("enter the shortform:")
a=key
if(month.has_key(a)):
	print "the next station is",  month[a] 
else:
	print "doent exist"

