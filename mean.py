import sys 
sum = 0
n=0


#Trying something new
#Sum input values
for numberline in open('data.txt'):
	sum +=float(numberline)
	n +=1

print "This has got to be wrong:"
print sum/n


