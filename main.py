import time

try: 
	bpm = int(input("please enter bpm (beats per minute): ")) 
except ValueError:
	print('make sure you are inputting an integer!') 

try:
	timeSignature = int(input("please enter the top number of your time signature: "))
except ValueError:
	print('make sure you are inputting an integer!')

barTime = 1/bpm * 60 * timeSignature
rests = [] 
while True:
	rest = input()
	if rest != 'done': 
		rests.append(int(rest)) 
	else:
		break 
for i in range(len(rests)): 
	input() 
	time.sleep(rests[i] * barTime - barTime) 
	print('one bar left!') 
	time.sleep(barTime)
	print('go ahead!')
