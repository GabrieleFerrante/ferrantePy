a=int(input("Inserisci a: "))
b=int(input("Inserisci b: "))

#Calcolare la x

def trovax(a,b):
	x=0
	if (x!=0):
		return
	else:
		return x

x=trovax(a,b)
print(x)
#print("x è uguale a "+str(x)" e il piu grande tra i valori è " +  str(max(a,b,x)))

#Invertire i valori

def swap(a,b):
	c=a
	a=b
	b=c
	print("Ora a è uguale a " + str(a) + " e b è uguale a " + str(b))
	
swap(a,b)