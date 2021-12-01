import cv2
import random
import time
import dropbox
start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name,frame)
        result = False
    return img_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destoryAllWindows()
def upload_file(img_name):
    access_token = "Lb-CHFQFstEAAAAAAAAAASGB5nBW-JXqLgVaCo0SgbjEaPyA_8c-UkLuNe16f5Sl"
    file = img_counter
    file_from = file
    file_to = "/images/" + (img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file_uploaded")
def main():
    while(True):
        if((time.time()- start_time)>=10):
            name = take_snapshot()
            upload_file(name)
main()
