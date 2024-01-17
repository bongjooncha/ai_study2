import os

# 디렉토리 내의 모든 txt 파일에 대해 작업 수행
directory = './label'  # 실제 경로로 변경해주세요

# 파일 이름 대응 목록
name_mapping = {
    '01012001': 2,
    '01012002': 3,
    '01012003': 4,
    '01012004': 5,
    '01012005': 6,
    '01012006': 7,
    '01016012': 8,
    '01016014': 9,
    '02011009': 10,
    '02011010': 11,
    '02011014': 12,
    '02011020': 13,
    '02011023': 14,
    '02011031': 15,
    '02011034': 16,
    '02011036': 17,
    '02011038': 18,
    '04011003': 19,
    '04011005': 20,
    '04012003': 21,
    '04012006': 22,
    '06012004': 23,
    '06012012': 24,
    '06012013': 25,
    '06013003': 26,
    '07014001': 27,
    '08011003': 28,
    '08011004': 29,
    '08013003': 30,
    '08013004': 31,
    '08014001': 32,
    '12011003': 33,
    '12011004': 34,
    '12011006': 35,
    '12011008': 36,
    '12011009': 37,
    '12011011': 38,
    '12011013': 39,
    '12011014': 40,
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
                    parts[0] = str(replace_value)
                file.write(' '.join(parts) + '\n')
