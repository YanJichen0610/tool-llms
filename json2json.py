# 该文件夹用于处理各种json文件的变换
import os
from tools.processFile import *
from tools.processPath import *



def imgWithJson(img_path,
                qa_path,
                qa_save_path,
                img_root=''):
    '''
    说明: 在大的qa数据集中寻找与当前图片匹配的qa并转成json
    '''
    qa_list = readJson(qa_path,id2data=True)
    img_id_list = readPath(img_path,with_root=False,with_suffix=False)

    qa_list_result = []

    for img_id in img_id_list:
        if img_id in list(qa_list.keys()):
            qa_list[img_id]['image'] = os.path.join(img_root,qa_list[img_id]['image'])
            qa_list_result.append(qa_list[img_id])

    saveJson(qa_save_path,qa_list_result)
    


if __name__ == '__main__':
    imgWithJson(
        r'img',
        r'llava_instruct_80k.json',
        r'qa.json'
    )