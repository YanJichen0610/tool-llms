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
        json.dump(data, f, ensure_ascii=False, indent=4)