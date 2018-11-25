import numpy as np
import io
import os
import string
import cv2
ans = []
def detect_text(path):

   
    img = cv2.imread("test.jpg")
    
    #裁切範圍
    x = 0
    y = 0

    w = 600
    h = 60

  
    crop_img = img[y:y+h, x:x+w]
   

    cv2.imwrite('crop.jpg', crop_img)
    
    #引用google api
    from google.cloud import vision
    from google.cloud.vision import types

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/opt/lampp/htdocs/upload/ainurse-ddf01edb5c56.json"  # key
    client = vision.ImageAnnotatorClient()
    

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

   
    for text in texts:

        an = text.description
        ans.append(an)
    for i in range(1,6):
        ans[i]= ans[i].replace("(","")
        ans[i]= ans[i].replace(")","")
    return (ans[2])


print(detect_text("/opt/lampp/htdocs/upload/crop.jpg"))
