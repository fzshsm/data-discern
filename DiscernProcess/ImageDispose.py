# -*- coding: utf-8 -*-

import os,shutil
import config
from PIL import Image

IMAGE_CONFIG = config.IMAGE
IMAGE_CROP = config.IMAGE_CROP

class ImageDispose(object):

    def readDataImage(self , gameId):
        path = IMAGE_CONFIG.get('temp') + '/' + gameId
        return os.listdir(path)


    def _getTempPath(self , gameId):
        path = IMAGE_CONFIG.get('temp') + '/' + gameId
        if(os.path.exists(path) == False):
            os.makedirs(path)
        return path

    def _deleteTempPath(self , gameId):
        path = IMAGE_CONFIG.get('temp') + '/' + gameId
        if(os.path.exists(path)):
            shutil.rmtree(path)
        return True

    def crop(self  , image):
        # img = Image.open(IMAGE_CONFIG.get('path') + image)
        img = Image.open(image)
        row = 0
        column = 0
        x = IMAGE_CROP.get('x')[0]
        y = IMAGE_CROP.get('y').get('begin')
        while y < IMAGE_CONFIG.get('height'):
            #纵向
            while x < IMAGE_CONFIG.get('width'):
                #横向
                gameId = image.split('/')[-1].split('.')[0]
                smallImgName = self._getTempPath(gameId) + "/%s%s.jpg" % ( row , column )
                if(column > 2):
                    y = IMAGE_CROP.get('y').get('whBegin') + row * ( IMAGE_CROP.get('wh') + IMAGE_CROP.get('y').get('whOffset'))
                    if(column == 3):
                        width = IMAGE_CROP.get('width')
                        height = IMAGE_CROP.get('height')
                    else:
                        width = IMAGE_CROP.get('wh')
                        height = IMAGE_CROP.get('wh')
                else:
                    y = IMAGE_CROP.get('y').get('begin') + row * IMAGE_CROP.get('y').get('offset')
                    width = IMAGE_CROP.get('width')
                    height = IMAGE_CROP.get('height')
                left = x
                top = y
                right = left + width
                bottom = top + height
                smallImg = img.crop((left , top , right , bottom))
                smallImg.save(smallImgName)
                column += 1
                if(column >= len(IMAGE_CROP.get('x'))):
                    break
                x = IMAGE_CROP.get('x')[column]
                # print ('row : %s  y: %s' % (row , y))
            x = IMAGE_CROP.get('x')[0]
            y += IMAGE_CROP.get('y').get('offset')
            column = 0
            row += 1

if __name__ == '__main__':
    ImageDispose = ImageDispose()

#imageDispose = ImageDispose()
# imageDispose.crop('/201710/18/8/1003.jpg')
#data = imageDispose.readDataImage("1003");
#print(data)
