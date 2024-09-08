from PIL import Image
import os

def convert_bmp_to_jpg(folder_path):
    # 遍历指定文件夹中的所有文件
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.bmp'):
            bmp_path = os.path.join(folder_path, file_name)
            jpg_path = os.path.join(folder_path, file_name.replace('.bmp', '.jpg'))

            with Image.open(bmp_path) as img:
                img = img.convert('RGB')
                img.save(jpg_path, 'JPEG')

            # 删除原始的 BMP 文件
            os.remove(bmp_path)


if __name__ == "__main__":
    folder_path = r"这里写入文件夹路径，前面的r不用删去"
    convert_bmp_to_jpg(folder_path)