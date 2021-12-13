#Import modules
import classes as cl
import data_parser as dp

print('Entered main program')
text=dp.data_loader("class.txt")
list1,list2=dp.dict1(text) 

listm=[]
listh=[]
listp=[]

print(list1)
for x in range(len(list1)):
	if list1[x]['class']=='Student':
		i=cl.Student(list1[x]['name'],list1[x]['lastname'],list1[x]['age'],list1[x]['rost'],list1[x]['score_m'],list1[x]['score_h'],list1[x]['score_p'])
		#listm.append(list1[x]['score_m'])
		listm.append(i)
		#listh.append(list1[x]['score_h'])
		listh.append(i)
		#listp.append(list1[x]['score_p'])
		listp.append(i)
		print(i.print_info())

for x in range(len(list2)):
	if list2[x]['class']=='Teacher':
		l=cl.Teacher(list2[x]['name'],list2[x]['lastname'],list2[x]['age'],list2[x]['rost'],list2[x]['predmet'])
		print(l.print_info())

#maximum
maxm=None
maxp=None
maxh=None
maxinfm=None
maxinfh=None
maxinfp=None
print(listh)
print(listp)
print(listm)
for items in listm:
	if maxm is None or i.score_m>maxm:
		maxm=i.score_m
		maxinfm=i.name+' '+i.lastname
print('Max Math: ', maxm, maxinfm)

for item in listh:
	if maxh is None or i.score_h>maxh:
		maxh=i.score_h
		maxinfh=i.name+' '+i.lastname
print("Max History: ",maxh,maxinfh)

for item in listp:
		if maxp is None or i.score_p>maxp:
			maxp=i.score_p
			maxinfp=i.name+' '+i.lastname
print('Max Prog: ',maxp,maxinfp)
