import pytesseract
import cv2
import numpy as np
import requests
import os
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('Test5.png')#will change this so photos can be user input
img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2=img.copy()
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
hi,wi=img2.shape
box=pytesseract.image_to_boxes(img)
#rectangles are made here which is not important
for b in box.splitlines():
    b=b.split(" ")
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img2,(x,hi-y),(w,hi-h),(0,255,0),2)
cv2.imshow('Frame',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#junk clearing from text found
txt = pytesseract.image_to_string(img, lang='eng')
txt = txt[:-1]
txt = txt.replace('\n', ' ')
if len(txt)<=10:
    main_query_final=txt
else:
    main_query=txt.split(".")
    main_query_final=main_query[0]+main_query[1]
#main_query=main_query[1][2::]
print(main_query_final)
#the book finding api
base_url = "https://www.googleapis.com/books/v1/volumes?"
#hiding the api key in environment variables
url = f"https://www.googleapis.com/books/v1/volumes?q={main_query_final}&key={os.environ.get('API_KEY')}"
response = requests.get(url).json()
book_last=""
for i in range (5):
    book_name=response['items'][i]['volumeInfo']['title']
    author_name=response['items'][i]['volumeInfo']['authors']
    book_description=response['items'][i]['volumeInfo']['description']
    #fixed a little so no redundant results are there
    if book_name!=book_last:
        print(book_name,"by",author_name[0])
        print("Description:")
        print(book_description)
    book_last=book_name