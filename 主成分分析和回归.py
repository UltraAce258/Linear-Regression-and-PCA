# 主成分分析和回归

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm

# 先进行主成分分析

# 读取标准化数据并提取自变量
data = pd.read_excel("C:/Users/美滋滋/Desktop/Scaled_Data.xlsx")

# 选择自变量
X = data[['X1', 'X2', 'X3', 'X4', 'X5', 'X6']]

# 数据已提前进行标准化, 故直接应用PCA
scaler = StandardScaler()
pca = PCA(n_components=len(X.columns))
X_pca = pca.fit_transform(X)

# 输出每个主成分的方差解释比和累积解释比
explained_variance_ratios = pca.explained_variance_ratio_
cumulative_variance = 0    # 后面用遍历循环的方法求累积解释比，故先赋值为0
print("\n","\n")
print("          解释的方差            ")
print("================================")
print("主成分   方差解释比   累积解释比")
print("--------------------------------")
for i, ratio in enumerate(explained_variance_ratios):
    cumulative_variance += ratio
    print("{:^5}     {:^.3%}".format(i, ratio),"    ","{:^.3%}".format(cumulative_variance))
print("================================")

# 打印主成分表达式
print("\n","\n")
print('前n个主成分的表达式')
for i, component in enumerate(pca.components_):
    expression = "F{} = ({:.8f}) * X1 + ({:.8f}) * X2 + ({:.8f}) * X3 + ({:.8f}) * X4 + ({:.8f}) * X5+ ({:.8f}) * X6".format(i, *component)
    print(expression)
    if i + 1 == 3:  # 如果想保留前三个主成分，等式右边就是3
        break

    
# 创建一个 DataFrame 来存储主成分的系数，并写入指定 Excel 文件
components = pca.components_
components_transposed = components.T    # 把数组转置，使列指标为各主成分
components_df = pd.DataFrame(components.T, columns=['F0', 'F1', 'F2', 'F3', 'F4', 'F5'])
column_labels = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6']    # 添加一列来标注行指标，行指标为各自变量
components_df.insert(loc=0, column='自变量\\系数\\主成分', value=column_labels)
output_file_path = "C:/Users/美滋滋/Desktop/F_Coefficients.xlsx"   # 指定文件
components_df.to_excel(output_file_path, index=False)   # 写入的 Excel 中不包括 DataFrame 的索引

print("前n个主成分的系数已写入文件 {}".format(output_file_path))


# 计算前三个主成分的值
F0_values = X_pca[:, 0]  # 第一个主成分 F0 的值
F1_values = X_pca[:, 1]  # 第二个主成分 F1 的值
F2_values = X_pca[:, 2]  # 第三个主成分 F2 的值


# 创建一个 DataFrame 来存储主成分的值，并写入指定 Excel 文件
result_df = pd.DataFrame({'F0': F0_values, 'F1': F1_values, 'F2': F2_values})

# 将结果写入 Excel 文件
output_file_path = "C:/Users/美滋滋/Desktop/F_Values.xlsx"   # 指定文件
result_df.to_excel(output_file_path, index=False)   # 写入的 Excel 中不包括 DataFrame 的索引

print("前n个主成分的值已写入文件 {}".format(output_file_path))
print("\n","\n")

# 下面进行主成分回归

try:
    a = eval(input("如果要继续对主成分和因变量进行回归，请输入“1”，否则输入“0”:"))
    if a == 1:
        
        # 读取标准化数据和主成分数据，提取主成分和标准化因变量
        data_1 = pd.read_excel("C:/Users/美滋滋/Desktop/Scaled_Data.xlsx")
        data_2 = pd.read_excel("C:/Users/美滋滋/Desktop/F_Values.xlsx")
        X = data_2[['F0', 'F1', 'F2']]  # 主成分
        Y = data_1['Y']  # 标准化因变量

        # 构建多元线性回归模型
        X = sm.add_constant(X)  # 添加常数项
        model = sm.OLS(Y, X)
        result = model.fit()

        # 查看回归系数
        print(result.summary())
    
        # 计算 Y 对 F0、F1、F2 的表达式
        print("\n","\n")
        coefficients = result.params  # 获取回归系数
        expression_Y = "Y = {:.8f} + {:.8f} * F0 + {:.8f} * F1 + {:.8f} * F2".format(
        coefficients['const'], coefficients['F0'], coefficients['F1'], coefficients['F2']
)
        print("Y 对 F0、F1、F2 的表达式为：")
        print(expression_Y)

        # 计算标准化变量的回归系数
        P_list = [coefficients['F0'], coefficients['F1'], coefficients['F2']]
        P_matrix = np.array(P_list).reshape(-1, 1)
        F_matrix = pca.components_[:3].T    # 把数组转置
        D = F_matrix@P_matrix    # @ 运算符用于矩阵乘法
        E = D.tolist()
        C = [item for sublist in E for item in sublist]    # 用列表推导式遍历 E 中的所有子列表，并将这些子列表中的所有元素收集到一个新的一维列表 C 中
        expression_Y = "Y = ({:.8f}) + ({:.8f}) * X1 + ({:.8f}) * X2 + ({:.8f}) * X3 + ({:.8f}) * X4 + ({:.8f}) * X5+ ({:.8f}) * X6".format(
coefficients['const'], C[0], C[1], C[2], C[3], C[4], C[5])
        print("\n","\n")
        print("Y 对 X1、X2、X3、X4、X5、X6 的表达式为：")
        print(expression_Y)

        # 提取系数
        C0, C1, C2, C3, C4, C5 = C[0], C[1], C[2], C[3], C[4], C[5]

        # 创建一个包含系数的 DataFrame
        coefficients_df = pd.DataFrame({
        'X': ['X1', 'X2', 'X3', 'X4', 'X5', 'X6'],
        'Y对自变量的系数': [C0, C1, C2, C3, C4, C5]
})

        # 将 DataFrame 写入 Excel 文件
        output_path = 'C:/Users/美滋滋/Desktop/Scaled_Coefficients.xlsx'
        coefficients_df.to_excel(output_path, index=False)

        print("系数已写入 {}".format(output_path))

except:
    pass


