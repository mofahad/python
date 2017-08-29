from sys import exit
more_stuff = ['Apple','Orange','mango','corn','banana']
stuff = more_stuff.pop()
print stuff
print stuff[-1]
#App = stuff.append();
#print App
asd = more_stuff   
print asd[-1]
print ' '.join(asd)
print '###'.join(asd)
print '__'.join(asd)
print '@@@'.join(asd)
dffd= asd.reverse()
print dffd
print "length of the asd : %d" %len(asd)
print "you are entered into the danger zone"
def death_race():

  print "u have to choose  a random no b\\w 0 and 100  :"
  give = raw_input('>>')
  if give in range(0,100):
   print "Divide it by 2 "
   dd = give/2
   print dd   
  else:
   print "thanks"
    
                               
def dead():
 print "This is the end//"
 exit(0)                               
print "Hello user u have two choice "
print "\n 1.  enter in the room"
print "\n 2. Otherwise leave the game "

def games():

 print " Hey there is two door take left or right"
 taken = raw_input('>>')
 if taken == "left":
  death_race()
 else :
  dead()
  
  
game ="""   _______________GAME HAS STARTED______________________________________
                        \n enter your choice. """
print game
ip  = raw_input('>>')
if "1" in ip:
  games()
else:
 print " Thank u!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
  

