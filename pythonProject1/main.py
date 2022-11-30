import cv2
from cvzone.HandTrackingModule import HandDetector

class Button:
    def __init__(self, pos, width, height, value):

        self.pos = pos
        self.width = width
        self.height = height
        self.value = value
    def draw(self, img):
        # Button part
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (50, 50, 50), 3)
        #cv2.rectangle(img, (100, 100), (200, 200), (50, 50, 50), 3)  # setting border
        cv2.putText(img, self.value, (self.pos[0] + 40, self.pos[1] + 60), cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    def checkclick(self,x,y):
        if self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (255, 255, 255),
                          cv2.FILLED)
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (50, 50, 50), 3)
            # cv2.rectangle(img, (100, 100), (200, 200), (50, 50, 50), 3)  # setting border
            cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 80), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0),
                        5)

            return True
        else:
            return False



# Webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280) # width
cap.set(4,720) # height
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Creting Buttons
buttonListValues = [['7','8','9','*'],
                    ['4','5','6','-'],
                    ['1','2','3','+'],
                    ['0','/','.','=']]
buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x*100 + 800
        ypos = y*100 + 150
        buttonList.append(Button((xpos,ypos),100,100,buttonListValues[y][x]))

# Variables
myEquation = ''
delayCounters = 0



# Loop
while True:
    # Get image from webcam
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Detection of the hand
    hands, img = detector.findHands(img, flipType=False)


    # Draw all buttons
    cv2.rectangle(img, (800,50), (800 + 400, 70 + 100), (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (800,50), (800 + 400, 70 + 100), (50, 50, 50), 3)
    for button in buttonList:
        button.draw(img)

    # Check for the HAND
    if hands:
        lmList = hands[0]['lmList']
        length, _, img = detector.findDistance(lmList[8],lmList[12], img)
        #print(length)
        x,y,z = lmList[8]
        if length < 75:
            for i,button in enumerate(buttonList):
                if button.checkclick(x,y) and delayCounters == 0:
                    myValue = buttonListValues[int(i%4)][int(i/4)]
                    if myValue == "=":
                        myEquation = str(eval(myEquation))
                    else:
                        myEquation += myValue
                        #myEquation = myEquation
                    delayCounters = 1

    # Avoid Duplicates
    if delayCounters != 0:
        delayCounters += 1
        if delayCounters > 10:
            delayCounters = 0


    # Display the Equation/result
    cv2.putText(img, myEquation, (810, 120), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)


    # Display iamge
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == ord('c'):
        myEquation = ''




