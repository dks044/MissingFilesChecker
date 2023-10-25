import os

def check_mp4_files(base_dir, num_required_files):
    missing_records = []
    
    # P01 ~ P10 폴더를 순회
    for parent_folder in range(1, 11):
        parent_folder_name = f"P{parent_folder:02}"  # P01, P02, ... , P10 형태
        parent_path = os.path.join(base_dir, parent_folder_name)

        if not os.path.exists(parent_path):
            continue

        # 해당 부모 폴더(P01 ~ P10) 내의 자식 폴더들을 순회
        for child_folder in os.listdir(parent_path):
            child_path = os.path.join(parent_path, child_folder)

            if os.path.isdir(child_path):
                # 자식 폴더 내의 mp4 파일 수를 카운트
                mp4_files = [file for file in os.listdir(child_path) if file.lower().endswith(".mp4")]

                # 21개가 아니라면 기록에 추가
                if len(mp4_files) != num_required_files:
                    missing_count = num_required_files - len(mp4_files)
                    missing_records.append(f"{base_dir} -> {parent_folder_name} -> {child_folder} 폴더가 MP4 파일이 {missing_count}개 부족함!")

    return missing_records

def main():
    base_dir = r"\\192.168.0.200\Lecple\2023년알앤디MP4\MP4\M4"
    num_required_files = 21
    records = check_mp4_files(base_dir, num_required_files)

    if records:
        with open("missing_mp4_records_M4.txt", "w", encoding="utf-8") as f:
            for record in records:
                f.write(record + "\n")
        print(f"MP4 파일이 부족한 폴더의 기록을 'missing_mp4_records.txt'에 저장했습니다.")
    else:
        print("모든 폴더에 MP4 파일이 21개씩 있습니다.")

if __name__ == "__main__":
    main()
