import cv2

def draw_boxes(image_path, label_path, output_path):
    image = cv2.imread(image_path)
    with open(label_path, 'r') as file:
        lines = file.readlines()

    height, width, _ = image.shape
    print(width, height)

    for line in lines:
        values = line.strip().split(' ')
        class_index = int(values[0])
        class_name = "0" if class_index == 0 else "1"  # 클래스 인덱스에 따라 클래스 이름 설정

        # 좌표를 픽셀 값으로 변환
        x_w, y_w, width_w, height_w = map(float, values[1:])
        x1 = int((x_w - width_w/2) * width)
        y1 = int((y_w - height_w/2) * height)
        x2 = int((x_w + width_w/2) * width)
        y2 = int((y_w + height_w/2)* height)
        
        # 직사각형 그리기
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 50)

        # 박스 우상단에 클래스 이름 표시
        cv2.putText(image, class_name, (x2, y1), cv2.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 30, cv2.LINE_AA)
    
    # 결과를 파일로 저장
    cv2.imwrite(output_path, image)

# 사용 예제
image_path = '01_011_01011001_160273203821324.jpeg'
label_path = '01_011_01011001_160273203821324.txt'
output_path = 'a.jpeg'

draw_boxes(image_path, label_path, output_path)
