import cv2
import numpy as np
import sys

name=sys.argv[1]
encrypted=sys.argv[2]
endSequence=sys.argv[3]
data=sys.argv[4]

def add(pixel, character):
    character=ord(character)
    character=bin(character)[2:]
    character=character.zfill(8)
    a=int(character[0:3], 2)
    b=int(character[3:6], 2)
    c=int(character[6:8], 2)
    pixel[0]=(pixel[0]//8)*8+a
    pixel[1]=(pixel[1]//8)*8+b
    pixel[2]=(pixel[2]//4)*4+c

def encrypt(image, data, endSequence):
    data+=endSequence
    m=len(image)
    n=len(image[0])
    index=0
    length=len(data)
    for i in range(m):
        for j in range(n):
            if index<length:
                add(image[i][j], data[index])
                index+=1
            else:
                return

image=np.array(cv2.imread(name))
encrypt(image, data, endSequence)
cv2.imwrite(encrypted, image)