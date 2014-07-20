import sys 
sum = 0
n=0


#Trying something new
#Sum input values
for num in open('data.txt'):
	sum +=float(num)
	n +=1

print sum/n


