#! /usr/bin/python

import argparse, sys, urllib2

def main(argv):
  # Handle options
  output = ""
  verbose = False
  parser = argparse.ArgumentParser()
  parser.add_argument("url", help="url or IP address to scan")
  parser.add_argument("-o", "--output", help="file to output to")
  parser.add_argument("-v", "--verbose", help="increased verbosity")
  args = parser.parse_args()
  if args.output:
     output = args.output
  if args.verbose:
     verbose = True

  # Start stuff for real
  req = urllib2.Request(args.url)
  f = urllib2.urlopen(req)
  print f.read()
  if output:
    print output

if __name__ =='__main__':
    main(sys.argv[1:])
