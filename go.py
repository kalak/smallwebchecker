#! /usr/bin/python

import getopt, sys

def usage():
  print "\nsmallwebchecker\n"
  print 'Usage: '+sys.argv[0]+' -u <url> [options]'
  print '	(Required)'
  print '	-u [url or IP address] : url to scan'
  print	'	(Optional)'
  print '	-o file : output to file instead of stdout'

def main(argv):
  # Handle options
  try:
    opts, args = getopt.getopt(argv, 'hu:o:', ['--url=', 'output='])
    if not opts:
      print 'No options supplied'
      usage()
  except getopt.GetoptError,e:
    print e
    usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt in ('-h', '--help'):
      usage()
      sys.exit(2)

  # Start stuff for real

if __name__ =='__main__':
    main(sys.argv[1:])