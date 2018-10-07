import os
import pprint
import argparse

pp = pprint.PrettyPrinter(indent=4)

parser = argparse.ArgumentParser(description="Highlight TODOs in multi-file tex document")

parser.add_argument('path', help="root directory of document")
parser.add_argument('-s', help="specify a single file to show")
parser.add_argument('-to', help="only show filenames and todos", action='store_true')
parser.add_argument('-so', help="only show filenames, subsections and todos", action='store_true')
#path = "/Users/matt/Documents/Conference/thesis/"


args = parser.parse_args()

#Tidy up path
if(args.path[-1:] != "/"):
    args.path = args.path + "/"

def find_tex(path):
    in_dir = os.listdir(path)
    tex_files = []
    for i in in_dir:
        if(i[0] != '.'):
            #print(path+i)
            if(os.path.isdir(path+i) == True):
                tex_files.extend(find_tex(path+i+"/"))
            elif(i[-4:] == '.tex'):
                tex_files.append(path+i)

    return tex_files

#Takes file object, highlights sections and TODOs
def file_searcher(args, file):
    line_count = 0
    for line in file:
        line_count += 1
        if (line[0:4] == "\\sec" and (not args.to or not args.so)):
            print('\033[91m' + "Section:  " + '\033[0m' + line[9:-2])
        elif (line[0:7] == "\\subsec" and not args.to):
            print('\033[33m' + "- Subsec:  " + '\033[0m' + line[12:-2])
        elif (line[0:7] == "\\subsub" and not args.to):
            print('\033[35m' + "-- Subsub:  " + '\033[0m' + line[15:-2])
        elif (line[0:5] == "%TODO"):
            print('\033[94m' + "Todo -> [" + str(line_count) + "] " + '\033[0m' + line[5:])

#If we select -s then just display that file
if(args.s != None):
    #Stat it first
    if(os.path.isfile(args.path + args.s) == True):
        with open(args.path+args.s, 'r') as file:
            print("*"*30)
            print(args.path+args.s)
            file_searcher(args, file)
    else:
        print("Error: Filename supplied is not a file")
        print(args.path + args.s)
else:
    #Else display them all
    tex_files = find_tex(args.path)
    for i in tex_files:
        with open(i, 'r') as file:
            print("*"*30)
            print(i)
            file_searcher(args, file)


