print "**********************************************************\n\n\t\t\tPrepei na vreis ton thisavro\n\n\n\n\t\t\tKanones paixnidiou:\n\nme kathe kinisi tha erxesai pio konta h pio makria sto key.\nskopo tou paixnidiou einai na ftaseis sto key\nme to W metakinise panw\nme to S katw\nme to A aristera\nme to D deksia"

#kataskevi labirinhtou

table=["player","key"]
for i in range(98):
	table.append(' ')
import random
random.shuffle(table)


#evresi player kai key

for i in range(100):
	if table[i]=="player":
		xplayer=i/10
		yplayer=i%10
	if table[i]=="key":
			xkey=i/10
			ykey=i%10
			
while (xplayer!=xkey or yplayer!=ykey):
	kinisi=""
	while (kinisi!="w" and kinisi!="W" and kinisi!="a" and kinisi!="A" and kinisi!="s" and kinisi!="S" and kinisi!="d" and kinisi!="D"):
		print "kante kinisi"
		kinisi=raw_input(':')		
	#Kanei kinisi 
	if (kinisi=="w" or kinisi=="W"):
		if  xplayer!=0:
			xplayer=xplayer-1
		elif xplayer==0:
			print "exeis piasei tavani, pigaine katw"	
	if (kinisi=="a" or kinisi=="A"):
		if yplayer!=0:
			yplayer=yplayer-1
		elif yplayer==0:
			print "den se pairnei aristera, mi to zwrizeis"
	if (kinisi=="s" or kinisi=="S"):
		if xplayer!=9:
			xplayer=xplayer+1
		elif xplayer==9:
			print "exeis piasei pato, pigaine panw"
	if (kinisi=="d" or kinisi=="D"):
		if yplayer!=9:
			yplayer=yplayer+1
		elif yplayer==9:
			print "den se pairnei deksia, mi to zwrizeis"
	apostasi=abs(xplayer-xkey)+abs(yplayer-ykey)
	if apostasi!=0:
		print "exeis akoma",apostasi,"kiniseis gia na ftaseis. \n"
print "eisai wraios re alani...to vrikes\n*****************************************************************"

