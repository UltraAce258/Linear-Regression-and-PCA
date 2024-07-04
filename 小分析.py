import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

# 读取数据并提取变量
data = pd.read_excel("C:/Users/美滋滋/Desktop/Little_Data.xlsx")
z = data[['z1', 'z2', 'z3']]

# 标准化数据
scaler = StandardScaler()
z_scaled = scaler.fit_transform(z)

# 创建一个新的 DataFrame 来存储标准化后的数据
result_df = pd.DataFrame({'Z1': z_scaled[:, 0],
                          'Z2': z_scaled[:, 1],
                          'Z3': z_scaled[:, 2],})

# 将结果写入 Excel 文件
output_file_path = "C:/Users/美滋滋/Desktop/Scaled_Little.xlsx"
result_df.to_excel(output_file_path, index=False)

print("标准化后的Z1、Z2、Z3 已写入文件 {}".format(output_file_path))


# 读取数据，并提取自变量
data = pd.read_excel("C:/Users/美滋滋/Desktop/Little_Data.xlsx")

# 
Z = data[['z1', 'z2', 'z3']]

# 计算皮尔逊相关系数
correlation_matrix = Z.corr()

# 输出相关系数矩阵
print("自变量相关性分析")
print('\n','\n')
print(correlation_matrix)


