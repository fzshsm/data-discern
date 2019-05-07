

import time
import os
from DiscernProcess import DataDiscern


SLEEP = 10


imgList = ["./temp/test/%s" % img for img in os.listdir('./temp/test')]
print(imgList)

discern = DataDiscern.DataDiscern()
data = discern.infer(imgList)
print(data)




# while True:
#     print(time.time())
#     time.sleep(SLEEP)
