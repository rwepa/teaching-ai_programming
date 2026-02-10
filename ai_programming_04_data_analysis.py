"""
File     : ai_programming_04_data_analysis.py
Title    : AI與程式語言-第4章 資料分析
Author   : Ming-Chang Lee
Email    : alan9956@gmail.com
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Encoding : UTF-8
"""

##############################
# 第4章 資料分析
##############################

##############################
# 大綱
##############################

# 4.0 下載 Anaconda
# 4.1 資料匯入探索
# 4.2 資料處理探索
# 4.3 資料視覺化探索

##############################
# 4.0 下載 Anaconda
##############################

# https://www.anaconda.com/download
# 按 [Free Download] \ 選取最底下頁面 [Download Miniconda Installer] \ 按左側 [Distribution Installers] \ 選取 Windows 下載
# 下載完成後, 直接按 [Enter] 進行安裝

##############################
# 4.1 資料匯入探索
##############################

# 寶可夢 Pokemon 資料示範
# 連結以下網頁, 按 右鍵 [Download raw file] 按鈕 \ 另存新檔 \ 存檔
# https://github.com/rwepa/DataDemo/blob/master/pokemon.csv

"""
# 寶可夢資料集說明
資料筆數: 894
欄位個數: 12
欄位名稱:
Number     寶可夢編號, 會有重複值
Name       名字
Type1      第1屬性
Type2      第2屬性
HP         血量
Attack     攻擊力
Defense    防禦力
SpecialAtk 特殊攻擊力
SpecialDef 特殊防禦力
Speed      速度
Generation 世代(1~7)
Legendary  是否為神獸(TRUE, FALSE)
"""

# 使用 pandas 模組進行資料匯入

import pandas as pd

# 匯入 CSV 檔案, 以 , 區隔者
# 依賁際下載位址,修改路徑.
path = "C:/Users/輸入使用者名稱/Downloads/pokemon.csv"
df = pd.read_csv(path)
df # 894*12

# 資料物件類別
type(df)
# pandas.core.frame.DataFrame 資料框(DataFrame)
# 資料框類似 Excel 工作表, 具有列指標與行指標, 可以選取多列與多行資料, 指標編號從0開始.

# NA 確認, Python 使用 nan 表示遺漏值 (missing value), 即 Excel 儲存格沒有輸入資料或輸入NA
# Type2 變數有421筆 nan 為遺漏值
df.isnull().sum()

# 前5筆
df.head()

# 後5筆
df.tail()

# 顯示指標(index)
df.index

# 欄名稱(columns)
df.columns

# 資料值(values)
df.values

# 資料摘要
df.describe()

# describe 統計摘要(statistic summary)
# count 個數
# mean  平均值
# std   標準差 standard deviation
# min   最小值
# 25%   25百分位數
# 50%   50百分位數, 中位數 median
# 75%   75百分位數 (quantile)
# max   最大值

# std 標準差
# https://en.wikipedia.org/wiki/Standard_deviation
# 一般希望愈小愈好, std=(sum(x-μ)^2/(n-1))^0.5

# 資料框訊息
df.info()

# 資料型態, int64 整數, object 字串, bool 布林值{True, False}
df.dtypes

# pandas 設定顯示所有欄位
pd.set_option('display.expand_frame_repr', False) # 取消自動換列
pd.set_option('display.max_columns', None)        # 設定直行完全顯示
pd.set_option('display.max_rows', None)           # 設定橫列完全顯示
df

##############################
# 4.2 資料處理探索
##############################

# axis 表示排序的軸，0表示 rows index(列指標)，1表示 columns index(行指標)
# 當對資料"列" 進行排序時，axis必須設置為0.
# ascending =FALSE, 即遞增是FALSE, 表示遞減是TRUE, 依欄位名稱遞減排序

df.sort_index(axis=1, ascending=False)

# 依照 Speed 欄大小, 由小至大排序 (預設值是遞增)
df_Speed_sort = df.sort_values(by='Speed')
df_Speed_sort

# 依照 Speed 欄大小, 改為由大至小排序, ascending=False 遞增是假的, 表示結果為遞減
df_Speed_descend = df.sort_values(by='Speed', ascending = False)
df_Speed_descend

# 依照 Type2 欄大小, 將 nan 排在最前面或最後面
df.sort_values(by='Type2')
df.sort_values(by='Type2', na_position = 'first')

# 選取行
# df['Hp'] # Error: Python 有區分英文大小寫

df['HP']
df.HP
df[['HP', 'Speed', 'Legendary']]

# 選取列
# df[0:4]選取第0列至第3列
# 列的編號從0開始, 記得 「:」符號的數字須減1, 即 4-1=3 表示列編號3的位置
df[0:4]

df[10:15] # 第10至第14列

# 使用 loc 函數 (loc: location)
# 資料物件[列指標, 行指標], 列指標使用 : 表示所有列的範圍
df.loc[:, ['HP', 'Speed', 'Legendary']]

# 注意: 不用15-1
df.loc[10:15, ['HP', 'Speed', 'Legendary']]

# 使用 iloc 函數 (iloc: index of location)
df.iloc[2] # 指標為第2列

df.iloc[2:4,]   # OK, 第2列至第3列(4-1)
df.iloc[2:4, :] # OK, 第2列至第3列(4-1)

# df.iloc[, 2]    # ERROR, 逗號之左側少了 「:」
df.iloc[:, 2]   # OK
df.iloc[:, 2:4] # OK, 第2行至第3行(4-1)

# 選取不連續範圍
df.iloc[[1,2,4],[0,1,3]]

# 選取某一儲存格資料
df.iloc[3, 6]

# 篩選條件
df_HP_gt100 = df[df.HP > 100]
df_HP_gt100

# 判斷何者為nan
pd.isnull(df)

# 刪除列中包括 NaN
df.dropna(how='any') # 程式執行完成, df 沒有改變

df.dropna(how='any', inplace = True) # 473*12, 程式執行完成, df 已經減少

# 建立資料框群組物件 DataFrameGroupBy
df_Type1 = df.groupby('Type1')

type(df_Type1) # pandas.core.groupby.generic.DataFrameGroupBy

# 依 Type1為群組, 計算 HP 的平均值
df_Type1[['HP']].mean()

# 依 Type1為群組, 計算 HP, Attack 二個變數的平均值
df_Type1[['HP', 'Attack']].mean()

# 將數值資料轉換為類別型資料
# 0 <=  HP < 55   -- > HP_small
# 55 <= HP < 85   -- > HP_middel
# 85 <= HP < 1000 -- > HP_large
# cut 函數中, right=False 表示右側區間沒有等號
df["HP_group"] = pd.cut(df.HP, list([0, 55, 85, 1000]), right=False, labels=['HP_small', 'HP_middle', 'HP_large'])
df.head(n=10)

##############################
# 4.3 資料視覺化探索
##############################

# 4.3.1 matplotlib 模組

# matplotlib 網頁
# https://matplotlib.org/

import matplotlib.pyplot as plt
import numpy as np

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 半徑 0~15

# 散佈圖(scatter)
# 方法1 plt方法
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title("X vs Y - scatter plot")
plt.xlabel("x")
plt.ylabel("y")

# 方法2 ax方法
fig, ax = plt.subplots()
ax.scatter(x, y, s=area, c=colors, alpha=0.5)
ax.set_xlabel(r'$\alpha_i$', fontsize=15)
ax.set_ylabel(r'$\beta_{i+1}$', fontsize=15)
ax.set_title('Alpha and beta change chart')
ax.grid(True)

# 儲存為 PNG, 以下3行一起執行
fig, ax = plt.subplots()
ax.scatter(x, y, s=area, c=colors, alpha=0.5)
fig.savefig('random.plot.png')

# 儲存為 PDF
fig, ax = plt.subplots()
ax.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.savefig('random.plot.pdf')

# 寶可夢 HP vs. Attack 散佈圖
fig, ax = plt.subplots()
ax.scatter(df.HP, df.Attack, s=df.Defense, c=df.Speed, alpha=0.5)
ax.set_xlabel('HP', fontsize=15)
ax.set_ylabel('Attack', fontsize=15)
ax.set_title('HP vs. Attack Scatter Plot')

# 寶可夢 HP vs. Defense 散佈圖
plt.scatter(df.HP, df.Defense)
fig, ax = plt.subplots()
ax.scatter(df.HP, df.Defense, s=df.Defense, c=df.Speed)
ax.set_xlabel('HP', fontsize=15)
ax.set_ylabel('Defense', fontsize=15)
ax.set_title('HP vs. Defense Scatter Plot')

# 直方圖 (histogram)
n, bins, patches = plt.hist(df.HP, 50, density=True, facecolor='b', alpha=0.75)
plt.xlabel('HP')
plt.ylabel('Probability')
plt.title('Histogram of HP')
plt.text(150, 0.025, r'$\mu=71.2,\ \sigma=23.9$')
plt.grid(True)

# 4.3.2 seaborn 模組

# seaborn 網頁
# https://seaborn.pydata.org/

import seaborn as sns

# 使用預設佈景主題 (theme)
sns.set_theme()

# 散佈圖
sns.relplot(
    data=df,
    x="HP", y="Attack"
)

# 群組散佈圖
sns.relplot(
    data=df,
    x="HP", y="Attack", 
    col="Legendary"
)

# 群組迴歸包括95%信賴區間
sns.lmplot(data=df, 
           x="HP", y="Attack",
           hue="Legendary").set(title='Grouped regression with 95% Confidence Interval')

# 直方圖
sns.displot(data=df, x="HP")

# 群組直方圖
sns.displot(data=df, x="HP", col="Legendary")

# 群組直方圖+核密度曲線(Kernel Density Estimation, KDE)
sns.displot(data=df, x="HP", col="Legendary", kde=True)

# 散佈圖矩陣 (Scatter Plot Matrix)
sns.pairplot(data=df.loc[:,'HP':'Speed'])
# end
