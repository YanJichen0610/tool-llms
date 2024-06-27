import pandas as pd
import csv

def save_dicts_to_csv_incrementally(data, csv_file_path):
    """
    将包含字典的列表保存到一个 CSV 文件中，其中每个字典的键是列名，值是列值

    参数:
    - data (list): 包含字典的列表，每个字典的键是列名，值是列值
    - csv_file_path (str): 保存 CSV 文件的路径
    """
    # 初始化一个布尔变量以指示是否已写入标题
        
    # 将字典转换为 DataFrame
    df = pd.DataFrame([data])
    
    # 追加写入 CSV 文件
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        df.to_csv(file, index=False, header=False)

# 示例数据
data = [
    [{'colomn1': 'value1'}, {'colomn2': 'value2'}],
    [{'colomn1': 'value3'}, {'colomn2': 'value4'}],
    [{'colomn1': 'value5'}, {'colomn2': 'value6'}]
]

