# import cv2
#
# # To read the image
# # img = cv2.imread('playersAndBall.jpeg')
# # 0 for id camara
# threshold = 0.5
# # cap = cv2.VideoCapture(0)
#
# classNames = []
# classFile = 'coco.names'
# with open(classFile, 'rt') as f:
#     classNames = f.read().rstrip('\n').split('\n')
#
# configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
# weightsPath = 'frozen_inference_graph.pb'
#
# net = cv2.dnn_DetectionModel(weightsPath, configPath)
# net.setInputSize(320, 320)
# net.setInputScale(1.0 / 127.5)
# net.setInputMean((127.5, 127.5, 127.5))
# net.setInputSwapRB(True)
#
# while True:
#     url = "http://10.100.102.23:8080/video"
#     cap = cv2.VideoCapture(url)
#     cap.set(3, 400)
#     cap.set(4, 200)
#     success, img = cap.read()
#     classIds, confs, bbox = net.detect(img, confThreshold=threshold)
#     # classIds is from coco.names
#     print(classIds, bbox)
#
#     if len(classIds) != 0:
#         for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
#             cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
#             cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
#                         (0, 255, 0), 2)
#             cv2.putText(img, str(round(confidence*100, 2)), (box[0] + 150, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
#                         (0, 255, 0), 2)
#
#     # To show the image
#     cv2.imshow("Output", img)
#     cv2.waitKey(0)


import cv2

thres = 0.5  # Threshold to detect object

cap = cv2.VideoCapture("http://192.168.1.16:8080/video")
cap.set(3, 1280)
cap.set(4, 720)
cap.set(10, 70)

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    success, img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold=thres)
    # print(classIds, bbox)

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
            cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            # cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
            #             cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    # while True:
    cv2.imshow("Output", img)
    cv2.waitKey(1)
