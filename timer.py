import turtle as t1
t = t1.Turtle()
t1.Screen().bgcolor('black')
t1.color('white')
t1.speed(100000)
t1.width(10)
t1.title('timer')
# import the time module
import time,math,os
os.system('cls||clear')
times = []
# define the countdown func.
def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		times.append('{:02d}:{:02d}'.format(mins, secs))
		t -= 1
	


def AfterTimer():
	#input('Want to logout?')
	#os.system('shutdown -l -f')
	print('Timer Done!!!!!!!!!!')

# input time in seconds
hours = 0
minutes = 1
seconds = 10
second = hours * (60*60) + minutes * 60 + seconds
#print(second)
size = 56
# function call
countdown(second)
#print(times)
for i in times:
	try:
		t1.clearscreen()
	except:
		AfterTimer()
		exit()
	timed = str(int(math.floor(int(i.split(':')[0])/60)>=1)*math.floor(int(i.split(':')[0])/60)) + ':'
	#print(timed)
	timed += str(int(i.split(':')[0])-(int(timed.split(':')[0])*60))
	timed += ':'
	timed += str(i.split(':')[1])
	if timed.split(':')[0]=='0':
		timed = timed.split(':')[1] + ':' + timed.split(':')[2]
	try:
		t.write(timed,font=("Arial", size, "normal"))
	except:
		AfterTimer()
		exit()
	time.sleep(1)
try:
	t1.clearscreen()
	t.write('0:00', font=("Arial", size, "normal"))
except:
	AfterTimer()
	exit()
AfterTimer()