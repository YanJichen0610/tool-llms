import os
from tools.processFile import *
from tools.processPath import *
from tqdm import tqdm 

def imgWithJson(img_path,
                qa_path,
                qa_save_path,
                img_root=''):
    '''
    说明: 在大的qa数据集中寻找与当前图片匹配的qa并转成json
    input: 
    - img_path: 图片信息
    - qa_path: 原始qa文件的路径
    - qa_save_path: 输出的qa文件路径信息
    '''
    
    qa_list = readJson(qa_path,id2data=True)
    img_id_list = readPath(img_path,with_root=False,with_suffix=False)

    qa_list_result = []

    # 使用tqdm包裹循环以添加进度条
    for img_id in tqdm(img_id_list):
        if img_id in list(qa_list.keys()):
            qa_list[img_id]['image'] = os.path.join(img_root,qa_list[img_id]['image'])
            qa_list_result.append(qa_list[img_id])

    saveJson(qa_save_path,qa_list_result)
    

if __name__ == '__main__':
    imgWithJson(
        r'/home/yanjichen/LLaVA/playground/data/coco_base/train2017',
        r'/home/yanjichen/LLaVA/playground/data/llava_instruct_150k.json',
        r'/home/yanjichen/LLaVA/playground/qa_data/coco_qa.json',
        r'/coco_base/train2017'  # 注意：最后一个参数前缺少逗号，在实际调用中应修正此语法错误
    )
