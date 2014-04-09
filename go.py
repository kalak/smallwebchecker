#! /usr/bin/python

import argparse, sys, urllib2

def main(argv):
  # Handle options
  outputfile = ""
  output = ""
  verbose = False
  parser = argparse.ArgumentParser()
  parser.add_argument("url", help="url or IP address to scan")
  parser.add_argument("-o", "--output", help="file to output to")
  parser.add_argument("-v", "--verbose", help="increased verbosity")
  args = parser.parse_args()
  if args.output:
     outputfile = args.output
  if args.verbose:
     verbose = True

  # Start stuff for real  
  try: 
    req = urllib2.Request(args.url)
    f = urllib2.urlopen(req)
    #output = f.read()
    # get headers: web server and web language, versions
    # get robots.txt
    # find possible cms
      # find cms version
      # find plugins
  except ValueError:
    print "Invalid URL"
    sys.exit(-1)



  # Print to file
  if outputfile:
    f = open(outputfile, 'w')
    f.write(output)
    f.close
  else:
    print output

if __name__ =='__main__':
    main(sys.argv[1:])
