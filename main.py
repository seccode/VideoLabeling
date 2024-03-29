import cv2
import argparse
import os
import time
'''
This script is meant for labeling of data with two classes.
If you are training a model with more than two classes, add
waitKeys that will represent other classes
'''

parser = argparse.ArgumentParser(description='Input args')
parser.add_argument('--video',dest='video',help='Path to input video')
parser.add_argument('--classes',dest='classes',type=str,help='Names of classes')

args = parser.parse_args()
class_1 = args.classes.split(',')[0]
class_2 = args.classes.split(',')[1]

if not os.path.isdir(class_1+'/'):
	os.mkdir(class_1)

if not os.path.isdir(class_2+'/'):
	os.mkdir(class_2)

video_path = args.video

cap = cv2.VideoCapture(video_path)

pic_count = 0
while True:
	ret, frame = cap.read()
	if not ret:
		break
	cv2.imshow('frame',frame)
	time.sleep(.1)
	key = cv2.waitKey(1)
	if key == 27: # Break on esc key
		break
	elif key == ord('1'):
		# Class 1 label
		cv2.imwrite(class_1+'/'+class_1+'_'+video_path.split('/')[-1].split('.')[0]+'_'+str(pic_count)+'.jpg',frame)
		pic_count += 1
		continue
	elif key == ord('2'):
		# Class 2 label
		cv2.imwrite(class_2+'/'+class_2+'_'+video_path.split('/')[-1].split('.')[0]+'_'+str(pic_count)+'.jpg',frame)
		pic_count += 1
		continue
