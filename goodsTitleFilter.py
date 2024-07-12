# 用于分析是否过滤该图片
import os
from tools.processFile import *
#from tools.processPath import *
from llm_tools.chineseClip import *
from tqdm import tqdm 

def SaveImgInfoV1(file_path, img_info_save_root):
    data = pd.read_csv(file_path)
    data = data.to_dict(orient='records')
    # print(data)
    img_dict_list = []  # 使用列表来收集每个图片的信息字典
    
    model,processor = cnClipModel("/apps/dat/cv/vlg/model/pretrain/cn-clip-vit-large-patch14-336")
    good_case = ["商品卖点信息","商品特性说明"]
    bad_case = ['服装尺码信息展示图','服装尺码对照表','商品商标','商品使用详细说明','店铺展示']
       
    
    for i, d in enumerate(tqdm(data[:100], desc="Processing images")):
        img_dict = {}
        # 商品图片的url
        url = {'url': d['商品图片']}
        # 商品图片的title
        caption = {'text': d['商品名称']}
        # 商品图片与文本关联性的分析分数
        sim = {'sim_score': None}
        good_case = ["商品卖点信息","商品特性说明","商品特点","商品采用技术"]
        good_case = good_case + [d['商品名称']]
        bad_case = ['服装尺码信息展示图','服装尺码对照表','产品尺码选择','鞋码选择','衣物标签','商品商标','商品使用细节详细说明','商品纯文本说明','店铺展示','门店展示','产品参数对照信息',"全球门店展示","全国门店展示"]
        score = cnClipSim(model,processor,good_case,bad_case,d['商品图片'])
        #print(score)
        score = score[0][:len(good_case)]
        sim = {'sim_score': sum(score)}
        print(sim)
        
        img_dict.update(url)
        img_dict.update(caption)
        img_dict.update(sim)

        print(img_dict)
        if i == 0:
            saveCSV(img_info_save_root, img_dict, mode='a', header=True)
        else:
            saveCSV(img_info_save_root, img_dict, mode='a', header=False)

            
if __name__ == '__main__':
    # r'/home/llms/jichen/deal_table/tabel/table/output_filename_1.xlsx'
    # '/home/llms/jichen/deal_table/tabel/table/output_filename.csv'
    SaveImgInfoV1(
    r'/home/llms/jichen/deal_table/tabel/table/output_filename.csv',
    r'goodcase_predict_smi.csv',
    )
    
