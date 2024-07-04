# 多元线性回归

import pandas as pd
import statsmodels.api as sm

# 读取数据并提取变量
data = pd.read_excel("C:/Users/美滋滋/Desktop/Scaled_Data.xlsx")
X = data[['X1', 'X2', 'X3', 'X4', 'X5', 'X6']]    # X 为自变量
Y = data['Y']    # Y 为因变量

# 添加截距项
X = sm.add_constant(X)  # 若数据已经过标准化，也可不添加截距项

# 拟合多元线性回归模型
model = sm.OLS(Y, X).fit()

# 打印回归结果
print(model.summary())
