import os

def remove_spaces_recursively(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            full_path = os.path.join(root, filename)
            new_filename = filename.replace(" ", "")  # 可以根据需要更改替换字符串
            new_full_path = os.path.join(root, new_filename)

            # 如果文件名发生变化，重命名文件
            if filename != new_filename:
                os.rename(full_path, new_full_path)
                print(f'Renamed: {full_path} -> {new_full_path}')

# 替换为您的目录路径
target_directory = r"D:\blog\docs\JohnTom1.github.io\docs\md"

# 执行文件名处理
remove_spaces_recursively(target_directory)
