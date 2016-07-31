import sys
import os

def find_files(abs_dir, query):
    for root, dirs, files in os.walk(abs_dir):
        for file in files:
            if file.endswith(".java") or file.endswith(".xml"):
                file_path = os.path.join(root, file)
                if query in open(file_path).read():
                    print file_path


if __name__ == "__main__": 
    if(len(sys.argv) <= 2):
        print "Please provide a absolute directory and query"
    elif(len(sys.argv) == 3):
        abs_dir = sys.argv[1]
        query = sys.argv[2]
        find_files(abs_dir, query)
    else:
        print "What's wrong with you!!!!"