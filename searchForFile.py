
import os, glob
from datetime import datetime
import sys

a = str(sys.argv[1])
path = a
#path = '/home/yassine/Desktop/ocr/'

nbr_item = 0
with open(os.path.join(os.environ.get('HOME'),'Desktop/files.txt'), 'w') as fl:
	for dirpath, dirnames, filenames in os.walk(path):
	    if len(sys.argv) > 2:
	       os.chdir(dirpath)
	       f = glob.glob(str(sys.argv[2]))      
	       if len(f) > 0 :
		 nbr_item += len(f) 
		 print 'Current path: ', dirpath
		 print 'File: ', f
		 print '------------------------------------'
		 
		 fl.write('\n')
		 fl.write('Current path: '+str(dirpath))
		 fl.write('\n')
		 fl.write('File: '+ str(f))
		 fl.write('\n')
		 fl.write('--------------------------')
	    else:
	       print 'Current path: ', dirpath
	       print 'Directories: ', dirnames
	       print 'File: ', filenames
	       print '------------------------------------'  
	if nbr_item > 0:
	   print "# files "+str(sys.argv[2])+":", nbr_item
           fl.write("\n# files "+str(sys.argv[2])+":"+ str(nbr_item))    

