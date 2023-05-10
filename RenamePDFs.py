#!/usr/bin/python3
import os, sys, argparse, subprocess
from colorama import Fore, Back, Style
import pdftitle
from pypdf import PdfReader
from pathvalidate import sanitize_filepath
import unidecode
SOURCE_DIR="KeepPDFhere"
TARGET_DIR="Done"
#############################################################################
def parse_args():
    parser = argparse.ArgumentParser(description="Rename PDF papers based on article titles")
    
    parser.add_argument('--ieee', '-i',
                        action='store_true',
                        #required=True, # comment if debugging with ipython
                        help="Article Type=IEEE",
                        default=False)
    parser.add_argument('--acm', '-a',
                        action='store_true',
                        help="Article Type=ACM",
                        default=False)
    parser.add_argument('--springer', '-s',
                        action='store_true',
                        help="Article Type=Springer",
                        default=False)
    
    args = parser.parse_args()
    return args
#############################################################################
args=parse_args()
#############################################################################
def getValidFileName(title):
    fpath = "%s.pdf"%(title)
    #print("{} -> {}".format(fpath, sanitize_filepath(fpath)))
    return(sanitize_filepath(fpath))
#############################################################################
def renameFile(src,dst):
    print(src,"--->",dst)
    os.rename(src, dst)
#############################################################################
def getTitle(page):
    text = page.extract_text().split("\n")
    text_dict={i:t for i,t in enumerate(text) if(t.isprintable())}
    key=list(text_dict.keys())[0]
    title=text_dict[key]
    return(None)
#############################################################################
''' STUB
args.ieee=True
args.acm=True
args.springer=True
'''
#############################################################################
listoffiles=[file for file in os.listdir(TARGET_DIR)]
for file in os.listdir(SOURCE_DIR):
    if file.endswith(".pdf"):
        PATH=os.path.join(SOURCE_DIR, file)
        try:
            title=pdftitle.get_title_from_file(PATH)
            new_title=getValidFileName(title)
            renameFile(PATH,TARGET_DIR+"/"+new_title)
        except:
            print(Fore.RED + "Attention: Some issue with file [%s]"%PATH)
            #print(Back.GREEN + 'and with a green background')
            #print(Style.DIM + 'and in dim text')
            print(Style.RESET_ALL)
            #print('back to normal now')
            pass
        #reader = PdfReader(PATH)
        #number_of_pages = len(reader.pages)
        #print(PATH," having ",number_of_pages, " pages")
        #page = reader.pages[0]
        #title=getTitle(page)


