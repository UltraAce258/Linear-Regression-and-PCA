# 数据标准化

import pandas as pd
from sklearn.preprocessing import StandardScaler

# 读取原始数据并提取变量
data = pd.read_excel("C:/Users/美滋滋/Desktop/Original_Data.xlsx")
v = data[['y', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6']]

# 标准化数据
scaler = StandardScaler()
v_scaled = scaler.fit_transform(v)

# 创建一个新的 DataFrame 来存储标准化后的数据，并写入指定 Excel 文件
result_df = pd.DataFrame({'Y': v_scaled[:, 0],
                          'X1': v_scaled[:, 1],
                          'X2': v_scaled[:, 2],
                          'X3': v_scaled[:, 3],
                          'X4': v_scaled[:, 4],
                          'X5': v_scaled[:, 5],
                          'X6': v_scaled[:, 6]})

output_file_path = "C:/Users/美滋滋/Desktop/Scaled_Data.xlsx"  # 指定文件
result_df.to_excel(output_file_path, index=False)  # 写入的 Excel 中不包括 DataFrame 的索引
print("标准化后的变量Y, X1, X2, X3, X4, X5, X6 已写入文件 {}".format(output_file_path))

# 计算均值和标准差
v_mean = v.mean()
v_std = v.std()

# 创建一个新的 DataFrame 来存储均值和标准差，并写入指定 Excel 文件
result_df = pd.DataFrame({'指标': ['均值', '标准差'],
                          'y': [v_mean['y'], v_std['y']],
                          'x1': [v_mean['x1'], v_std['x1']],
                          'x2': [v_mean['x2'], v_std['x2']],
                          'x3': [v_mean['x3'], v_std['x3']],
                          'x4': [v_mean['x4'], v_std['x4']],
                          'x5': [v_mean['x5'], v_std['x5']],
                          'x6': [v_mean['x6'], v_std['x6']]})
output_file_path = "C:/Users/美滋滋/Desktop/Means&Average.xlsx"  # 指定文件
result_df.to_excel(output_file_path, index=False)  # 写入的 Excel 中不包括 DataFrame 的索引
print("均值和标准差已写入文件已写入文件 {}".format(output_file_path))
