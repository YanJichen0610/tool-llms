<<<<<<< HEAD
import os
import json
import requests
import pandas as pd



def downloadImage(url, save_path):
    """
    下载图片并保存到指定路径

    参数:
    - url (str): 图片的URL地址
    - save_path (str): 保存图片的路径
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果请求不成功，抛出HTTPError

        # 确保保存目录存在
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with open(save_path, 'wb') as file:
            file.write(response.content)

        #print(f"图片已保存到 {save_path}")
    except requests.RequestException as e:
        print(f"下载图片时出错: {e}")



def readJson(file_path,id2data=False):
    '''
    说明: 用于读取json文件
    input: 
    - id2data: 时候要转成id2data格式
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    if id2data == True:
        data = {d['id']:d for d in data}
    return data



def readCSV(file_path):
    """
    读取 CSV 文件并将其内容转换为字典列表。
    
    参数:
    file_path (str): CSV 文件的路径。
    
    返回:
    list of dict: 每个字典代表 CSV 文件中的一行，键是列名，值是对应列的值。
    """
    # 使用 pandas 读取 CSV 文件
    df = pd.read_csv(file_path)
    
    # 将 DataFrame 转换为字典列表
    data_list = df.to_dict(orient='records')
    
    return data_list



def saveCSV(file_path,dict,mode=None,header=False):
    '''
    说明: 用于存储csv文件
    input:
    - file_path: 储存路径
    - dict: 需要储存数据, 为字典格式
    - mode: 时候使用其他存储模式, 假如是一次性存储的话没必要修改此参数
    '''
    if mode == 'a':
        temp_df = pd.DataFrame([dict])
        temp_df.to_csv('image_info.csv', mode='a', header=header, index=False)




def saveJson(file_path,data):
    '''
    说明: 用于储存json文件
    input:
    - file_path: 储存路径
    - data: 需要储存的数据
    '''
    with open(file_path, 'w', encoding='utf-8') as f:
=======
import json



def readJson(file_path,id2data=False):
    '''
    说明: 用于读取json文件
    input: 
    - id2data: 时候要转成id2data格式
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    if id2data == True:
        data = {d['id']:d for d in data}
    return data

def saveJson(file_path,data):
    '''
    说明: 用于储存json文件
    input:
    - file_path: 储存路径
    - data: 需要储存的数据
    '''
    with open(file_path, 'w', encoding='utf-8') as f:
>>>>>>> f4bf1b57f1bc9ec48bf6b1f0ca8bbddba051e38a
        json.dump(data, f, ensure_ascii=False, indent=4)