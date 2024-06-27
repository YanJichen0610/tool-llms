import csv
import os
from tqdm import tqdm
from tools.processFile import *

def saveCSV(file_path, data_dict, mode='a', header=False):
    """
    保存字典数据到 CSV 文件
    """
    with open(file_path, mode, newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data_dict.keys())
        if header:
            writer.writeheader()
        writer.writerow(data_dict)

def SaveImgInfo(file_path, img_save_root, img_info_save_root, sim_output=False):
    '''
    说明: 基于url下载图片并保存
    input: 
    - file_path: 训练数据路径
    - img_save_root: 图片保存根目录路径
    - img_info_save_root: 图片信息保存根目录路径
    '''
    data = readCSV(file_path)
    img_dict_list = []  # 使用列表来收集每个图片的信息字典

    # 使用 tqdm 添加进度条
    for i, d in enumerate(tqdm(data[:10], desc="Processing images")):
        img_dict = {}  # 为每个条目创建一个新的字典
        url = {'url': None}
        img_save_path = {'img_save_path': None}
        caption = {'text': None}
        sim = {'sim': None}

        if 'url' in d:
            url = {'url': d['url']}
        if 'filename' in d:
            img_save_path_value = os.path.join(img_save_root, d['filename'])
            downloadImage(url=d['url'], save_path=img_save_path_value)  # 解注释此行以启用图片下载
            img_save_path = {'img_save_path': img_save_path_value}

        if 'text' in d:
            caption = {'text': d['text']}

        if sim_output:
            sim = {'sim': d['sim']}

        img_dict.update(url)
        img_dict.update(img_save_path)
        img_dict.update(caption)
        img_dict.update(sim)
        

        if i == 0:
            saveCSV(img_info_save_root, img_dict, mode='a', header=True)
        else:
            saveCSV(img_info_save_root, img_dict, mode='a', header=False)

if __name__ == '__main__':
    SaveImgInfo(
        r'test-2.6w.csv',
        r'img',
        r'test.csv'
    )
