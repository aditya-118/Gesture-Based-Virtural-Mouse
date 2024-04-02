import cv2 as cv
import os
import time

#argument 0 is given to use the default camera of the laptop
camera = cv.VideoCapture(0)

#Now check if the camera object is created successfully
if not camera.isOpened():
    print("The Camera is not Opened....Exiting")
    exit()
else:
    print("Camera captured")

#creating a list of labels "You could add as many you want"
Labels = []

ans= 'Y'

while ans == 'Y':
    print("Enter Gesture Name")
    Labels.append(input())
    print("Do you wish to continue")
    ans=input()

print("Gestures to be recorded are")
for label in Labels:
    print(label)

DatasetDir = 'C:\\Users\\bansa\\Project\\Gesture-Controlled-Virtual-Mouse\\Dataset\\'
print(os.listdir(DatasetDir))
#Now create folders for each label to store images
for label in Labels:
    if not os.path.exists(DatasetDir+label):
        os.makedirs(DatasetDir+label)
        
    #using count variable to name the images in the dataset.
    count = 0    
    print("Sleeping for ten seconds")
    time.sleep(10)
    
    #Taking input to start the capturing
    print("Start data collection for " + label)
    
    #clicking 5 images per label, you could change as you want.
    while count<200:
        #read returns two values one is the exit code and other is the frame
        status, frame = camera.read()
        
        #check if we get the frame or not
        if not status:
            print("Frame is not been captured..Exiting...")
            break
        
        #display window with gray image
        cv.imshow("Video Window", frame)
        
        #Store the image to specific label folder
        cv.imwrite(label+'/img'+str(count)+'.png',frame)
        count += 1
        # to quit the display window press 'q'
        if cv.waitKey(5) & 0xFF == 13:
                break

# When everything done, release the capture
camera.release()
cv.destroyAllWindows()