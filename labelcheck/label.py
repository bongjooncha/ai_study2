import os

# 디렉토리 내의 모든 txt 파일에 대해 작업 수행
directory = '/path/to/your/directory'  # 실제 경로로 변경해주세요

# 파일 이름 대응 목록
name_mapping = {
    '01012001': 2,
    '01012002': 3,
    '01012003': 4,
    # ... 나머지 매핑 추가 ...
}

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)

        # 파일 이름에 대응되는 값 가져오기
        file_key = filename.split('_')[2]
        replace_value = name_mapping.get(file_key, 1)  # 기본값은 1

        # 파일 내용 수정
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # 수정된 내용 저장
        with open(file_path, 'w') as file:
            for line in lines:
                parts = line.split()
                if parts and parts[0] == '1':
                    parts[1] = str(replace_value)
                file.write(' '.join(parts) + '\n')
