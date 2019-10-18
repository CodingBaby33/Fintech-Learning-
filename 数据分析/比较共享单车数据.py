#数据分析流程
#明确任务-数据搜集（爬虫，公开数据集）-数据处理-数据分析-结果展示
#数据 csv后缀，用逗号隔开各个特征，每行代表一个样本
# 数据描述，有四个季度的数据，每个季度有多个样本
import os
import numpy as np

data_path = ' '#存放数据集的文件夹
data_filenames = [' ',' ']

def collect_data():
  data_arr_list = []#将四个季度的数据放在list里
  for data_filename in data_filenames:#对某一个季度的样本进行处理
    data_file = os.path.join(data_path,data_filename)#获取完整的文件路径
    data_arr = np.loadtxt(data_file,delimiter = ',' ,dtype='str',skiprows=1)
    data_arr_list.append(data_arr)
  return data_arr_list


def process_data(data_arr_list):
    duration_in_list =[] 
    for data_arr in data_arr_list:
      duration_str_col = data_arr[:,0]
      #去掉双引号
      duration_in_ms = np.core.defchararray.replace(duration_str_col,'"',' ')
      #类型转换 转换成float
      duration_in_ms.astype('float')
    return duration_in_list
  
 def analyze_data(data_arr_list):
    duration_mean_list =[]
    for i,duration in enumerate(data_arr_list):#enumerate 能够将索引号返回出来
      duration_mean = np.mean(duration)
      print('{}average:{:.2f}min',format(i+1,duration_mean))
      duration_mean_list.append(duration_mean)
    return duration_mean_list
  
 def show_result(duration_mean_list):
  plt.figure()
  plt.bar(range(len(duration_mean_list)),duration_mean_list)
  plt.show()
    
      
def main():
  data_arr_list = collect_data()
  duration_list = process_data(data_arr_list)
  duration_mean_list = analyze_data(duration_list)
  show_results(duration_mean_list)
  
  duration_list = process_data(data_arr_list) 
  
  
      
  
