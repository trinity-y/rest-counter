import time //library import so we can waiiiiiit a minute 

try: // make sure nobody ends up entering a LETTER VALUE or something!
	bpm = int(input("please enter bpm (beats per minute): ")) //takes in that t e m p o
except ValueError:
	print('make sure you are inputting an integer!') // gotta tell em what they're doing wrong

try: //gottta cheeckk again

	timeSignature = int(input("please enter the top number of your time signature: ")) //now for the time signature
except ValueError:
	print('make sure you are inputting an integer!')

barTime = 1/bpm * 60 * timeSignature // divide by bpm by 60. now you've got your bps. now multiply by how many beats are in a bar. ta da!!
rests = [] // all your rest queues 
while True: //repeats till broken !
	rest = input()
	if rest != 'done': // keeps repeating till the entry isn't 'done'.
		rests.append(int(rest)) // appends in entry to the rest queue list
	else:
		break // whaM! it's BROKEN!
for i in range(len(rests)): // repeat this till you're done yer rest queues
	input() // waits for that niiiice enter
	time.sleep(rests[i] * barTime - barTime) // rest till the bar warning
	print('one bar left!') // yes the br warning
	time.sleep(barTime) // now one moree
	print('go ahead!') // yYYAYy .! loop if there's more !!
  //le fin ;)
