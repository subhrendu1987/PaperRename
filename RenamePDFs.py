from pypdf import PdfReader
from pathvalidate import sanitize_filepath
import os, sys, argparse
TARGET_DIR="KeepPDFhere"
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
def checkValid(title):
	fpath = "%s.pdf"%(title)
	print("{} -> {}".format(fpath, sanitize_filepath(fpath)))
	return(sanitize_filepath(fpath))
#############################################################################
def renameFile(src,dst):
	print(src,"--->",dst)
#############################################################################
def getTitle(page):
	text = page.extract_text().split("\n")
	text_dict={i:t for i,t in enumerate(text) if(t.isprintable())}
	key=list(text_dict.keys())[0]
	title=text_dict[key]
	return(title)
#############################################################################
''' STUB
args.ieee=True
args.acm=True
args.springer=True
'''
#############################################################################
for file in os.listdir(TARGET_DIR):
    if file.endswith(".pdf"):
        PATH=os.path.join(TARGET_DIR, file)
        reader = PdfReader(PATH)
        number_of_pages = len(reader.pages)
        print(PATH," having ",number_of_pages, " pages")
        page = reader.pages[0]
        title=getTitle(page)
        if(checkValid(title)):
        	renameFile(PATH,TARGET_DIR+"/"+title+".pdf")

