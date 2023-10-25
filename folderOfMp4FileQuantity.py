import os

def count_mp4_files(directory):
    mp4_count = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".mp4"):
                mp4_count += 1
    
    return mp4_count

directory = r"\\192.168.0.200\Lecple\2023년알앤디MP4\MP4"
total_mp4_files = count_mp4_files(directory)
print(f"{directory} 폴더와 그 하위 폴더에 있는 .mp4 파일 수: {total_mp4_files}개")
