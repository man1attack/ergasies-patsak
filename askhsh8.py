import random
mylist=[(random.randint(-30,30))for k in range (30)]
j=-1
a=[0]*28
for i in range(28):
	if (mylist[i]+mylist[i+1]+mylist[i+2])==0:
		j=j+1
		a[j]=i
if j==-1:
	print "Stathikes Atyxos :( .Isws thn epomenh fora."
else:
	if j==0:
		print "Yparxei Monadiki 3ada :) "
	else :
		print "Yparxoyn ",(j+1)," 3ades :) "
for i in range (j+1):
	print (mylist[a[i]]),(mylist[a[i]+1]),(mylist[a[i]+2])
	