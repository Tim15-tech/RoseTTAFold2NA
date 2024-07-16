import argparse
import re

def run():
    parser = argparse.ArgumentParser(description='Make every character in an afa-file AUCGN-like')
    parser.add_argument('afa-filename', type=str,
                        help='path to the afa-file')
    filepath = vars(parser.parse_args())['afa-filename']
    print(filepath)
    replaceFunction(filepath)

def replaceFunction(filepath: str):
    # in lace rewriting difficult to to linepointers
    # as files are big content should be stored and saved line by line
    strippedPath = filepath[:-4] # strips .afa
    print(strippedPath)
    with open(filepath, 'r+') as f:
        with open(strippedPath+"Cleared.afa", 'w') as f2:
            for line in f:
                newline = ""
                if line[0] != '>':
                    for i in line:
                        if i not in ['A', 'C', 'G', 'U', "\n", "-", 'N', '0']:
                            newline += 'N'
                        else:
                            newline += i
                else:
                    newline += line
                f2.write(newline)
        
        

if __name__ == "__main__":
    run()