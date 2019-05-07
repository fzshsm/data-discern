import os
import config
from DiscernProcess import ImageDispose


imageDispose = ImageDispose.ImageDispose()

imageRootPath = 'D:/image'
a = 1
for yearMonth in os.listdir(imageRootPath):
    oneLevel = imageRootPath + '/' + yearMonth
    for date in os.listdir(oneLevel) :
        secLevel = oneLevel + '/' + date
        for league in os.listdir(secLevel) :
            thirdLevel = secLevel + '/' + league
            for imageFile in os.listdir(thirdLevel):
                imagePath = thirdLevel + '/' + imageFile
                a += 1
                print(imagePath)
                imageDispose.crop(imagePath)



print(a)