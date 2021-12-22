import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.videoCapture(0)
    result=True
    while(result):
        #read frames while camera is on
        ret,frame=videoCaptureObject.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        start_time=time.time

        result=False
    return imageName
    print("snapshotTaken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(imageName):
    access_token="FIrp80p3OmoAAAAAAAAAAcIAEe2Ft-17jCEPBmrrJ8kd1zyRr7kIRF9NdE1G7ABi"
    file= img_counter
    file_from=file
    file_to="/capturedImage/"+(imageName)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("files uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)

main()                   