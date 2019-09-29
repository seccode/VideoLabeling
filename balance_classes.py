import glob
from sklearn.model_selection import train_test_split
import argparse
import os

parser = argparse.ArgumentParser(description='Input args')
parser.add_argument('--classes',dest='classes',type=str,help='Names of classes')

args = parser.parse_args()
class_1 = args.classes.split(',')[0]
class_2 = args.classes.split(',')[1]

files_1 = glob.glob(class_1+'/*')
files_2 = glob.glob(class_2+'/*')

if len(files_1) == 0:
    print("No folder of name {} found".format(class_1))
if len(files_2) == 0:
    print("No folder of name {} found".format(class_2))

if len(files_1) > len(files_2):
    rem, keep = train_test_split(files_1,test_size=len(files_2)/len(files_1))
    for file in files_1:
        if file in rem:
            os.remove(file)
else:
    rem, keep = train_test_split(files_2,test_size=len(files_1)/len(files_2))
    for file in files_2:
        if file in rem:
            os.remove(file)






#
