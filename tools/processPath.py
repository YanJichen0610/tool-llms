import os



def readPath(root,with_root=True,with_suffix=True):
    '''
    说明: 读取指定路径下的文件路径
    input:
    - root: 指定路径
    - with_root: 返回时时候包含指定的路径
    - with_suffix: 返回时时候包含文件后缀
    '''
    path_list = [p for p in os.listdir(root)]

    if with_root == True:
        path_list = [os.path.join(root,p) for p in path_list]
    if with_suffix == False:
        path_list = [p.split('.')[0] for p in path_list]

    return path_list