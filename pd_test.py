import pandas as pd


import os

Dir_path = os.path.abspath(__file__)
def get_task(path, sh_name):
    data = pd.DataFrame(pd.read_excel(path, sheet_name=sh_name))  # 获得每一个sheet中的内容
    tasks_list = list(set(data['任务单号']))
    tasks_list.sort()
    print('任务单号', tasks_list)
    return tasks_list,data


def get_distance_to_excle(tasks_list,data):
    write = pd.ExcelWriter(Dir_path + '/结果.xlsx')
    for task_id in tasks_list:
        result = data.loc[data['任务单号'] == task_id]  # 指定任务单号的货物清单
        shop_list = list(set(result['商品货格'])) + ['FH03', 'FH11']  # 商品货格清单
        print('任务单号', task_id)
        print('商品货格', shop_list)
        print(len(shop_list))
        database_excel_path = Dir_path + '/data.xlsx'
        database_excel_name = 'distance'
        database = pd.DataFrame(
            pd.read_excel(database_excel_path, sheet_name=database_excel_name))  # 获得每一个sheet中的内容  # 读取data Excel表
        database = database.set_index('Unnamed: 0')
        task_id_excel = database.loc[shop_list, shop_list]
        task_id_excel.to_excel(write, sheet_name=str(task_id), index=True)



# print(data.index)

# print(data.loc[['A'],['x']])          #表示选取所有的行以及columns为a,b的列；
# print(data.loc[['A','B'],['x','z']])     #表示选取'A'和'B'这两行以及columns为x,z的列的并集；
if __name__ == '__main__':
    # path = Dir_path + '/附件1：仓库数据.xlsx'  # 附件4：计算结果.xlsx
    # sh_name = '任务单'
    # task_list,data = get_task(path, sh_name)
    # task_list = task_list[0:6] # 取前6个订单号
    # get_distance_to_excle(task_list,data)


    path = "/Users/zhangbai/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/8aeac8580f8eb4fb2c41f7d6f853f02b/Message/MessageTemp/c5a56229d4c2171ed51e25e0c132b2ad/File/附件1：总行部门员工信息统计表(1).xls"

    # path = Dir_path + '/ttt.xlsx'  # 附件4：计算结果.xlsx
    data = pd.DataFrame(pd.read_excel(path, 1,keep_default_na=False))  # 获得每一个sheet中的内容
    data2 = data.set_index('招商银行XX部门隔离员工信息统计表')
    # print(data2)
    # e = data2.loc[['S01','S02'],['S02','S03']]
    # e.to_excel(Dir_path + '/结果.xlsx', index=True) # 索引是否显示
    # print(data)
    print(data2.index)
    print(data2.loc[['序号']])