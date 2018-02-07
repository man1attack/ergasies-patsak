import datetime

today=datetime.date.today()
dates=datetime.date(today.year,today.month,today.day)
j=0
k=today.year

for i in range (10):
	k=k+1
	dates=datetime.date(k,today.month,today.day)
	if today.isoweekday()==dates.isoweekday():
		j=j+1
		print "Tha yparksei kai alli tetoia mera to etos",k

if j==0:
	print "Den yparxei alli tetoia mera sta epomena 10 xronia"
else:
	print "Synolo einai ",j ,"fores sta 10 epomena xronia"

