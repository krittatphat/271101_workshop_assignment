import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 2:
                    id2 = int(id)
                    cx2 = cx
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 6:
                    id6 = int(id)
                    cy6 = cy
                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 14:
                    id14 = int(id)
                    cy14 = cy
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 10:
                    id10 = int(id)
                    cy10 = cy
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 18:
                    id18 = int(id)
                    cy18 = cy
                if id == 20:
                    id20 = int(id)
                    cx20 = cx

            if cx4 < cx20:
                if cx4 < cx2: 
                        cv2.putText(img, str("Thumb "), (10, 50), cv2.FONT_HERSHEY_PLAIN, 2,(4, 4, 207), 3)
            elif cx4 > cx20:
                if cx4 > cx2: 
                        cv2.putText(img, str("Thumb "), (10, 50), cv2.FONT_HERSHEY_PLAIN, 2,(4, 4, 207), 3)

            if cy8 < cy6:
                cv2.putText(img, str("Index "), (150, 50), cv2.FONT_HERSHEY_PLAIN, 2,(4, 4, 207), 3)

            if cy12 < cy10:
                cv2.putText(img, str("Middle"), (270, 50), cv2.FONT_HERSHEY_PLAIN, 2,(4, 4, 207), 3)

            if cy16 < cy14:
                cv2.putText(img, str("Ring  "), (400, 50), cv2.FONT_HERSHEY_PLAIN, 2,(4, 4, 207), 3)

            if cy20 < cy18:
                cv2.putText(img, str("Pinky "), (500, 50), cv2.FONT_HERSHEY_PLAIN, 2,(4, 4, 207), 3)
            else:
                 cv2.putText(img, str( ), (30, 70), cv2.FONT_HERSHEY_PLAIN, 2,(4, 4, 207), 2)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)