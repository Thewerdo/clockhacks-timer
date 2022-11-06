import time
import sys
from playsound import playsound

def delete_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
h=int(input('set amount of hours '))
delete_last_line()
x=int(input("set amount of minutes "))
delete_last_line()
s=int(input("set amount of seconds "))
delete_last_line()
thing = input('what is this timer for ')
delete_last_line()
while x>=0 and s>=0 and h>=0:
  time.sleep(1)
  if x==0 and s==0:
    x=60
    h-=1

  else:
    if s==0:
      s=59
      x-=1
      if h==0:
        if x==0:
          print(s,'seconds')
        else:
          print (x,'minutes',s,'seconds')
      else:
        print(h,'hours',x,"minutes",s,'seconds')
    else:
      s-=1
      if h==0:
        if x==0:
          print(s,'seconds')
        else:
          print (x,'minutes',s,'seconds')
      else:
        print(h,'hours',x,"minutes",s,'seconds')

  delete_last_line()

print('time for', thing)
playsound("1.wav")