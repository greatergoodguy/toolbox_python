import sys
import os
import re


def find_files(abs_dir, regex):
    pattern = re.compile(regex, re.DOTALL)

    print abs_dir

    for root, dirs, files in os.walk(abs_dir):
        for file in files:
            if file.endswith(".java") or file.endswith(".xml") or file.endswith(".txt"):
                file_path = os.path.join(root, file)

                # for i, line in enumerate(open(file_path)):
                #     for match in re.finditer(pattern, line):
                #         line_num = i + 1
                #         print file_path + ' Found on line %s' % line_num

                for match in re.finditer(pattern, open(file_path).read()):
                    print file_path
                    # print 'Found on line %s: %s' % (i+1, match.groups())

                # if query in open(file_path).read():
                #     print file_path


if __name__ == "__main__": 
    if(len(sys.argv) <= 2):
        print "Please provide a absolute directory and regex"
    elif(len(sys.argv) == 3):
        abs_dir = sys.argv[1]
        regex = sys.argv[2]
        find_files(abs_dir, regex)
    else:
        print "What's wrong with you!!!!"