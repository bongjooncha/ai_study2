import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

def visualize_and_save_coco_data(data, image_path, save_path):
    # 이미지 불러오기
    image = Image.open(image_path)

    # Matplotlib figure 생성
    fig, ax = plt.subplots()

    # 각 행의 데이터를 반복하면서 경계 상자를 그립니다.
    for row in data:
        class_id, x, y, width, height = row

        # 좌표를 이용하여 경계 상자 생성
        bbox = patches.Rectangle((x, y), width, height, linewidth=2, edgecolor='r', facecolor='none')

        # 경계 상자를 그림에 추가
        ax.add_patch(bbox)

        # 클래스 ID를 텍스트로 추가 (선택 사항)
        ax.text(x, y, f'Class {int(class_id)}', fontsize=8, color='r')

    # 그림을 보여줍니다.
    plt.imshow(image)
    plt.axis('off')

    # 그림을 파일로 저장합니다.
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1)
    plt.close()

# 주어진 데이터와 파일 경로로 시각화하고 이미지를 파일로 저장
data = [
    [0, 0.511460, 0.520374, 0.710526, 0.928693],
    [1, 0.499328, 0.546123, 0.455221, 0.569327]
]
image_path = '01_011_01011001_160273203821324.jpeg'  # 이미지 파일 경로
save_path = 'output_visualization.jpg'  # 저장할 파일 경로

visualize_and_save_coco_data(data, image_path, save_path)

