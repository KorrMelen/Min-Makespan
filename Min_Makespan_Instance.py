import random
def input_file(name_file):
	file = open(name_file,"r")
	instance = file.read()
	file.close()
	instance = instance.split(":")
	instance = map(lambda x : int(x),instance)

	M = [0]*instance[0]
	D = [0]*instance[1]

	for i in range(2,len(instance)):
		D[i-2] = instance[i]
	return D,M


def input_keyboard(instance):
	instance = instance.split(":")
	instance = map(lambda x : int(x),instance)

	M = [0]*instance[0]
	D = [0]*instance[1]

	for i in range(2,len(instance)):
		D[i-2] = instance[i]
	return D,M


def input_Im(m):
	M = [0]*m
	D = [0]*(2*m+1)
	D[0] = m
	for i in range(1,m,2):
		D[i] = D[i+1] = m+i
	return D,M


def input_Ir(m,n,k,minv,maxv):
	instances = []
	for i in range(k):
		D = [0]*m
		M = [0]*n
		for j in range(n):
			M[j] = random.randint(minv,maxv)
		instances.append((D,M))
	return instances