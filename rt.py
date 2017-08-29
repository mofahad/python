""" this comment and in this we are just writting the code of reading and writing files"""
from sys import argv
from os.path import exists

script,friend,gh = argv
print "Copying from %s to %s" % (friend, gh)
in_file = open(friend)
in_data = in_file.read()
print "The input file is %d bytes long" %len(in_data)
print "Does the output file exist? %r" % exists(gh)

out_file = open(gh , 'w')
out_file.write(in_data)
out_file.close()
in_file.close()


 
