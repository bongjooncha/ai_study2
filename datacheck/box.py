import cv2

def draw_boxes(image_path, label_path, output_path):
    image = cv2.imread(image_path)
    with open(label_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        values = line.strip().split(' ')
        class_index = int(values[0])
        x, y, width, height = map(float, values[1:])
        
        # 좌표를 픽셀 값으로 변환
        height, width, _ = image.shape
        x = int(float(x) * width)
        y = int(float(y) * height)
        width = int(width * width)
        height = int(height * height)
        
        # 객체의 경계 상자를 이미지에 그림
        cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
    
    # 결과를 파일로 저장
    cv2.imwrite(output_path, image)

# 사용 예제
image_path = '01_011_01011001_160273203821324.jpeg'
label_path = '01_011_01011001_160273203821324.txt'
output_path = 'a.jpeg'

draw_boxes(image_path, label_path, output_path)
