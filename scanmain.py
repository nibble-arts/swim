# encoding=utf-8
# SIM main programm
import sys, pickle, configparser

# from module import *
from module import *
import argparse

# get commandline args

'''
-h             help
-v             verbose
-r             scan recursive
-d,--depth     scan depth when -r; 0=without limit

-a,--album     album name
--album-root   set album root; mandatory for new album

--db-path      database path; default=data/
'''


parser = argparse.ArgumentParser(description='Server Side Image Management')
# parser.add_argument("--root",dest="root",type=str,help="album root path",required=True)
parser.add_argument("-v",dest="verbose",nargs="?",const=True,help="print details",default=False)
parser.add_argument("-r",dest="recurse",nargs="?",const=True,help="scan recursive")
parser.add_argument("-d","--depth",dest="depth",type=int,help="depth of recursive scan")

parser.add_argument("-a","--album",dest="album",type=str,help="album name",required=True)
parser.add_argument("--album-root",dest="albumRoot",type=str,help="set album root path")

parser.add_argument("-s","--start",dest="scanStart",type=str,help="scan start path in album root")

parser.add_argument("--db-path",dest="datapath",type=str,help="set database path; default=data/",default="data/")
parser.add_argument("--thumb-path",dest="thumbpath",type=str,help="set thumbnail path; default=thumb/",default="thumb/")
parser.add_argument("--thumb-size",dest="thumbsize",type=str,help="set thumbnail size; default=80",default="80")


args = vars(parser.parse_args())

# set args
verbose = args["verbose"]
albumName = args["album"]
dataPath = args["datapath"]

# if args["root"]:
# 	pass

'''
albumRoot = args["albumRoot"]
albumName = args["album"]

dataPath = args["datapath"]
thumbPath = args["thumbpath"]
thumbSize = args["thumbsize"]
'''


# load album database
# load album or add it
#   if not exist --album-root is necessarry
#   if exist --album-root changes root of album

album = album.Album(albumName,args,verbose)
print (album.album())



# set recursion level
if args["recurse"]:
	# set depth by -d parameter
	if args["depth"]:
		depth = args["depth"]
	# no parameter but -r => search all
	else:
		depth = 0

# no recursion -> set depth to 1
else:
	depth = 1

scanStart = args["scanStart"]


# create scanner
s = scan.Scanner(album)


# start scan
try:
	s.scan(subdir=scanStart,depth=depth,verbose=verbose)

	if verbose:
		print ("overall images indexed: ",s.len())

except KeyboardInterrupt:
	print ("\n\nindexing apported")
