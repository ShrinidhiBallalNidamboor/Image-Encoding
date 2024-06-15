import cv2
import numpy as np
import sys

encrypted=sys.argv[1]
endSequence=sys.argv[2]

def extract(pixel):
    a=pixel[0]%8
    b=pixel[1]%8
    c=pixel[2]%4
    character=a*32+b*4+c
    character=chr(character)
    return character
           
def decrypt(image, endSequence):
    a=len(endSequence)
    b=0
    endSequence=list(endSequence)
    sequence=[]
    data=''
    m=len(image)
    n=len(image[0])
    for i in range(m):
        for j in range(n):
            character=extract(image[i][j])
            if b<a:
                sequence.append(character)
                b+=1
            else:
                sequence.pop(0)
                sequence.append(character)
            data+=character
            if sequence==endSequence:
                return data[:-a]
    return data

image=np.array(cv2.imread(encrypted))
print(decrypt(image, endSequence))