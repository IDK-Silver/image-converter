import argparse
import os
from lib.image import open_image
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

def convert_image(args):
    input_path, output_path, output_format = args
    img = open_image(input_path)
    if img:
        img.save(output_path, format='JPEG' if output_format.lower() == 'jpg' else output_format.upper())
        print(f"已轉換: {os.path.basename(input_path)} -> {os.path.basename(output_path)}")

def convert_images(input_folders: list, output_folder: str, output_format: str, prefix: str = ""):
    """
    將指定資料夾中的所有圖片轉換為指定格式並輸出到指定資料夾。

    Args:
        input_folders (list): 輸入圖片的資料夾路徑列表
        output_folder (str): 輸出圖片的資料夾路徑
        output_format (str): 輸出圖片的格式（如 'jpg', 'png'）
        prefix (str, optional): 輸出圖片檔名的前綴（可選）。 Defaults to "".
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    tasks = []
    for input_folder in input_folders:
        for filename in os.listdir(input_folder):
            input_path = os.path.join(input_folder, filename)
            if os.path.isfile(input_path):
                output_filename = prefix + os.path.splitext(filename)[0] + '.' + output_format
                output_path = os.path.join(output_folder, output_filename)
                tasks.append((input_path, output_path, output_format))

    # 使用線程池處理，使用全部可用的 CPU 核心
    import multiprocessing
    max_workers = multiprocessing.cpu_count()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(convert_image, tasks)

def main():
    parser = argparse.ArgumentParser(description="將圖片轉換為指定格式")
    parser.add_argument("input_folders", nargs='+', help="輸入圖片的資料夾路徑（可以指定多個）")
    parser.add_argument("output_folder", help="輸出圖片的資料夾路徑")
    parser.add_argument("output_format", help="輸出圖片的格式（如 jpg, png）")
    parser.add_argument("--prefix", default="", help="輸出圖片檔名的前綴（可選）")

    args = parser.parse_args()

    convert_images(args.input_folders, args.output_folder, args.output_format, args.prefix)

if __name__ == "__main__":
    main()