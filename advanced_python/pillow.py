from PIL import Image
import requests
import time
im = Image.open(requests.get("https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/alsnwekruiaw8dlz9lco.jpg",stream=True).raw)
im.show()
time.sleep(5)
im.close()
img = Image.open(requests.get("https://image.cnbcfm.com/api/v1/image/105343415-1532101496379gettyimages-975924044.jpeg?v=1553790495",stream=True).raw)
time.sleep(5)
img.show()
img.close()