"""
File     : ai_programming_03_anaconda.py
Title    : AI與程式語言-第3章 Anaconda簡介與安裝
Author   : Ming-Chang Lee
Email    : alan9956@gmail.com
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Encoding : UTF-8
"""

##############################
# 第3章 Anaconda簡介與安裝
##############################

# 大綱
# 3.1 Python 簡介與安裝
# 3.2 Anaconda 簡介與安裝
# 3.3 Spyder 軟體簡介
# 3.4 變數
# 3.5 資料型別與運算子
# 3.6 資料物件
# 3.7 認識模組

##############################
# 3.1 Python 簡介與安裝
##############################

# Python 下載
# https://www.python.org/ 

help(print)
print('Hello world')
quit()

1+2

# Python 執行 <方法3> IDLE模式
"""
# helloworld.py
print("Python資料處理分析")
"""

# 已安裝模組
# pip list

# pandas 模組 - 線上說明
# python -c help('pandas')

"""
# RStudio – 執行 Python 
# 2022.9.6
# Click [Terminal]
# conda env list
# conda activate base
# python

# Ctrl + Alt + Enter
import pandas as pd
print(pd.__version__)
"""

##############################
# 3.2 Anaconda 簡介與安裝
##############################

# https://www.anaconda.com/

# 實作練習1
# 在 jupyter notebook 輸入以下程式碼練習
from numpy import *
random.rand(5,5)

# jupyter-notebook 更改預設目錄
# 程式集 \ Windows 系統 \ 命令提示字元
# cd C:\
# jupyter-notebook

# Jupyter Notebook 快速鍵
# 按 [Esc] cell旁邊為藍色
# 按 x：刪除當前選擇的cell
# 按 a：在當前選擇的上方新增一個cell
# 按 b：在當前選擇的下方新增一個cell
# 按 Shift + Enter：執行當前的cell並且選到下一個cell
# 按 Ctrl + Enter：執行當前cell
# 按 M：轉成markerdown模式，可以看到紅色框框內容從code變成markerdown

# 實作練習2
# 開啟下列 ipynb 檔案
# Python 程式設計-李明昌 <免費電子書>
# http://rwepa.blogspot.com/2020/02/pythonprogramminglee.html

# 安裝 Orange
# conda install -c conda-forge orange3

# 使用命令提示列 開啟 Orange
# python -m Orange.canvas

# Python Orange - 關聯規則教學
# http://rwepa.blogspot.com/2022/07/python-orange-associate-tutorial.html
# https://youtu.be/rh5GxJamtNg

# Anaconda 模組管理

# 顯示已安裝模組
# conda list

# 尋找官網套件
# conda search matplotlib

# 安裝模組
# conda install 模組名稱

# 更新模組
# conda update 模組名稱

# conda 虛擬環境

# 檢視所有虛擬環境清單 	conda env list
# 啟用 myenv 虛擬環境 	conda activate myenv
# 關閉虛擬環境 			conda deactivate
# 建立 myenv 虛擬環境 	conda create --name myenv
# 建立特定 python 版本的虛擬環境
# conda create -n myenv python=3.9
# 建立特定 scipy 模組版本的虛擬環境
# conda create -n myenv scipy=1.9.0

# 參考 https://github.com/rwepa/DataDemo/blob/10c8ab50a0871a6d30b212cef3fc865248532a39/iPAS-python-program.py#L2658

##############################
# 3.3 Spyder 軟體簡介
##############################

# Spyder 更新

# 步驟1.Anaconda 整體更新
# conda update anaconda

# 步驟2.Spyder 更新
# conda update spyder

# 實作練習3
# 熟悉自動換列等設定
# Tools \ Preferences \ Editor \ Display \ Wrap lines

# 恭喜您, 開啟 Python 學習之旅 ^_^

# Python 執行

# 方法1.命令提示列
# 建立 C:\mydata\helloworld.py

# cd C:\mydata
# python --version
# dir
# python helloworld.py

# 方法2.使用 Spyder

print("大數據Python應用")

##############################
# 3.4 變數
##############################

# 合法變數
CustomerSaleReport = 1
_CustomerSaleReport = 1
Customer_Sale_Report = 1
customer_sale_report = 1
大數據 = 1 # 中文亦可,建議不要使用

# 不合法變數
$CustomerSaleReport = 1 # SyntaxError: invalid syntax
2020_sale = 100 # SyntaxError: invalid decimal literal
break = 123 # SyntaxError: invalid syntax

# 內建保留字
dir(__builtins__)
len(dir(__builtins__)) # 160

# Python 註解
# 使用一個 #	 用於1行註解
# 使用二個 """  用於超過1行註解或函數之說明文件

# 內縮4個空白鍵之語法

##############################
# 3.5 資料型別與運算子
##############################

# 資料型別(資料型態)
# https://docs.python.org/3/library/stdtypes.html

# 資料型別-範例

# 整數 int
x1 = 1
type(x1)

# 浮點數 float
x2 = 1.234
type(x2)

# 複數  complex
x3 = 1+2j
type(x3)

# 布林值 (Boolean)
x4 = True
type(x4)
x4 + 10

# None值
import numpy as np
None == False
None == 0
False == 0
True == 1
None == np.nan
None == None

# 整數亂數
# https://docs.python.org/3/library/random.html
# randrange(start, stop[, step])
# 包括 start, 不包括stop
import random
random.seed(168)
myrandom = random.randrange(1, 100)
myrandom

# 運算子
3 + 5
3 + (5 * 4)
3 ** 2
"Hello" + "World"
1 + 1.234
7 / 2
7 // 2
7 % 2
2 ** 10
1.234e3 - 1000

x5 = 1 == 2
x5
x5 + 10

# 指派運算子
x = 9
x+=2  # 相同於 x = x+2 = 9+2=11
print(x)

##############################
# 3.6 資料物件
##############################

# 資料物件
# Tuple 序列 (元組) - (value,...) 不可修改
# List 串列(清單)   - [value,...]
# Set 集合          - {value,...}
# Dict 字典         - {key:value,...}

##############################
# Tuple 序列 (元組)
##############################

# 建立序列
f = (2,3,4,5) # A tuple of integers
g = () # An emptmy tuple
h = (2, [3,4], (10,11,12)) 	# A tuple containing mixed objects

# Tuples操作
x = f[1] # Element access. x = 3
x

y = f[1:3] # Slices. y = (3,4)
y

z = h[1][1] 	# Nesting. z = 4
z

# tuple - loop 處理
fruits = ("apple", "banana", "cherry")

# 方法1. tuple - 取出元素, 使用for
for x in fruits:
  print(x)

# 方法2. tuple - 取出元素, 使用while
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1
  
# 方法3. tuple - 取出元素, 使用指標 range, len
for i in range(len(fruits)):
  print(fruits[i])

##############################
# List 串列(清單)
##############################

# 建立串列
a = [2, 3, 4]            # 整數串列
b = [2, 7, 3.5, "Hello"] # 混合資料串列
c = []	                 # 空串列
d = [2, [a, b]]	         # 巢狀串列

# 串列的操作
a
a[1] 	   # 取得第2個元素
a[-1]      # 取得最後一個元素
b[1:3] 	   # 串列篩選
d[1][0][2] # 巢狀串列操作
b[0]       # 2
b[0] = 42  # 修改元素值
b[0]       # 42

# 串列長度
len(b)

##############################
# Set 集合
##############################

# 集合與字典相似, 但字典沒有key,只有值
# 集合內容不可以修改
# 集合是  unordered
# 集合是  unindexed
# 集合會忽略重複的值

a = set() # 空集合
type(a)

b = {"台北市", "新北市", "桃園市", "台中市", "台北市", "新北市", "高雄市"}
b # {'台中市', '台北市', '新北市', '桃園市', '高雄市'}

# b[0] = 1 # TypeError: 'set' object does not support item assignment
# b[0]     # TypeError: 'set' object is not subscriptable

len(b)

##############################
# Dict 字典
##############################

# 字典宣告
mydict = {
    "language": "Python",
    "designer": "Guido van Rossum",
    "year": 1991
    }

print(mydict)

type(mydict) # dict

# 重複 key, 只保留1個
mydict1 = {
    "language": "Python",
    "designer": "Guido van Rossum",
    "year": 1991,
    "year": 2021
    }

print(mydict1)

# 字典存取元素 – keys, values
b = {
     "uid": 168, 
     "login": "marvelous", 
     "name" : 'Alan Lee'
     }
b

# dict 取得所有 keys
mykeys = b.keys()
print(mykeys)

# dict 取得所有 values
myvalues = b.values()
print(myvalues)

# dict 取得key的值
u = b["uid"] # 168
print(u)

# dict 更新值
b.update({"uid": 123})
print(b)

# dict 新增元素
b["shell"] = "/bin/sh"
print(b)

##############################
# 3.7 認識模組
##############################

# 使用模組
import math
math.sqrt(9)

from math import sqrt
sqrt(9)

# 切換工作目錄
import os
os.getcwd() # 讀取工作目錄
os.chdir("C:/") # 變更工作目錄
os.getcwd()
os.listdir(os.getcwd()) # 顯示檔案清單

# 模組的搜尋路徑
import sys
sys.path
# '' 表示現行目錄

# 實作練習4
# 自訂模組, 計算商數與餘數
# 自訂模組檔案名稱為 numberscompute.py

# numberscompute.py
def divide(a,b):
	q = a/b        	# q 商數
	r = a - q*b  	# r 餘數
	return q,r

# 練習檔案名稱為 mycompute.py
import numberscompute
x,y = numberscompute.divide(42,5)

# 參考資料 -----

# RWEPA
# http://rwepa.blogspot.com/

# Python 程式設計-李明昌 <免費電子書>
# http://rwepa.blogspot.com/2020/02/pythonprogramminglee.html

# R入門資料分析與視覺化應用教學(付費)
# https://mastertalks.tw/products/r?ref=MCLEE

# R商業預測與應用(付費)
# https://mastertalks.tw/products/r-2?ref=MCLEE
# end
# 辛苦啦,完成Python程式之旅~~
