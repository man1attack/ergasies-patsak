import random


a=100*[100*[0]]

for i in range (100):
		a[i]=[random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(100)]

file_in=open("new.txt","r")
for line in file_in:
	for i in range (100):
		for j in range (100):
			if a[i][j]==line[0]:
				m=1
				for k in range (len(line)):
					if i+len(line)<99 and a[i+m][j]==line[k]:
						m=m+1
						if m==len(line)-1:
							print "H leksi ",line," ksekinaei apo to ",i,j," orizontia."
				for k in range (len(line)):
					if j+len(line)<99 and a[i][j+m]==line[k]:
						m=m+1
						if m==len(line)-1:	
							print "H leksi ",line," ksekinaei apo to ",i,j," katheta."

file_in.close()

