from ultralytics import YOLO
model = YOLO('./best.pt')

img = './picture/hard_pic2.jpg'

results=model(source=img)

print(results)
# for r in results:
#     print(results)