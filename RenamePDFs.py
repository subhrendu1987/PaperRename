from pypdf import PdfReader
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
                        default="False")
    parser.add_argument('--springer', '-s',
                        action='store_true',
                        help="Article Type=Springer",
                        default="False")
    
    args = parser.parse_args()
    return args
#############################################################################
for file in os.listdir(TARGET_DIR):
    if file.endswith(".pdf"):
        print(os.path.join(TARGET_DIR, file))
        reader = PdfReader(file)
        number_of_pages = len(reader.pages)
        #page = reader.pages[0]
        #text = page.extract_text()


