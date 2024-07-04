# 变量相关性分析

import pandas as pd

# 读取数据并提取变量
data = pd.read_excel("C:/Users/美滋滋/Desktop/Scaled_Data.xlsx")
V = data[['Y','X1', 'X2', 'X3', 'X4', 'X5', 'X6']]

# 计算皮尔逊相关系数
correlation_matrix = V.corr()

# 输出相关系数矩阵
print("变量相关性分析")
print('\n','\n')
print(correlation_matrix)

