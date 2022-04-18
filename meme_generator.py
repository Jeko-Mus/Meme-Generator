import cv2
import numpy as np
import matplotlib.pyplot as plt

# import image
meme = cv2.imread('img/dive.png')

# convert from BGR to RGB
rgb_meme = cv2.cvtColor(meme, cv2.COLOR_BGR2RGB)
cv2.imshow('rgb_meme', rgb_meme)
cv2.waitKey(0) 
#closing all open windows 
cv2.destroyAllWindows() 

# input text and text borders to create meme
meme_copy = rgb_meme.copy()
plt.figure(figsize = (10,8))
cv2.rectangle(meme_copy, (250,140), (580,100), (0,0,255), 1)
cv2.rectangle(meme_copy, (250,85), (530,20), (255,0,255), 1)
cv2.putText(meme_copy, 'Olympics', (250, 70), cv2.FONT_ITALIC, 2, (0,0,0))
cv2.putText(meme_copy, 'swim champion, first place', (250, 115), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0))
cv2.putText(meme_copy, '... i suppose dreams do come true!', (270, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0))
cv2.imshow('meme', meme_copy)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
