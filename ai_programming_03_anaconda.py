"""
File     : ai_programming_03_anaconda.py
Title    : AI與程式語言-第3章 Anaconda簡介與安裝
Author   : Ming-Chang Lee
Email    : alan9956@gmail.com
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Encoding : UTF-8
"""

# 大綱
# 3.1 Python 簡介與安裝
# 3.2 Anaconda 簡介與安裝
# 3.3 Spyder 軟體簡介
# 3.4 變數
# 3.5 資料型別與運算子
# 3.6 資料物件
# 3.7 認識模組
# 3.8 numpy模組

# 參考資料

# Python 程式設計-李明昌 免費電子書
# http://rwepa.blogspot.com/2020/02/pythonprogramminglee.html

# R參考資料
# R 入門資料分析與視覺化應用(7小時28分鐘)
# https://mastertalks.tw/products/r?ref=MCLEE

# R 商業預測應用(8小時53分鐘)
# https://mastertalks.tw/products/r-2?ref=MCLEE

##############################
# 資料分析架構APC方法
##############################
# 1.群組
# 2.時間
# 3.建立評估變數

# 2020新型冠狀病毒視覺化
# http://rwepa.blogspot.com/2020/02/2019nCoV.html

# shiny 顧客連接分析
# https://rwepa.shinyapps.io/shinyCustomerConnect/

# 品質管制圖(quality control chart)應用
# http://rwepa.blogspot.com/2021/10/r-shiny-quality-control-chart.html

# Taiwan Stock App
# https://rwepa.shinyapps.io/shinyStockVis/ 

##############################
# 第3章 Anaconda簡介與安裝
##############################

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

# 實作練習
# 在 jupyter notebook 輸入以下程式碼練習
from numpy import *
random.rand(5,5)

# jupyter-notebook 更改預設目錄
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

# 實作練習
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

# 實作練習
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

# 指派多個變數
x, y, z = "台北", "台中", "高雄"
print(x,y,z)
type(x) # str

address = ["台北", "台中", "高雄"]
x, y, z = address
print(x)
print(y)
print(z)

# Python Style Rules
# https://google.github.io/styleguide/pyguide.html

# Python 註解
# 使用一個 #	   用於1行註解
# 使用二個 """  用於超過1行註解或函數之說明文件

# 內縮4個空白鍵之語法

##############################
# 3.5 資料型別與運算子
##############################

# 資料型別(資料型態)
# https://docs.python.org/3/library/stdtypes.html

# 廣義資料型別
# Text Type:      str
# Numeric Types:  int, float, complex
# Boolean Type:	  bool
# Binary Types:	  bytes, bytearray, memoryview
# Sequence Types: list, tuple, range
# Set Types:	  set, frozenset
# Mapping Type:	  dict
# 參考: https://www.w3schools.com/python/

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

# 位移運算子: << 向左位移
# 位移運算子: >> 向右位移
a = 4 << 3 # 0100 --> 0100000, 32 16 8 4 2 1
print(a)

b = a * 4.5
print(b)

c = (a+b)/2.5

# 指派運算子
x = 9
x+=2
print(x)

##############################
# 3.6 資料物件
##############################

# 資料物件
# Tuple 序列 (元組) - (value,...) 不可變更
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

xy = (2, 3)
xy

personal = ('Hannah',14,5*12+6)
personal

singleton = ("hello",)
singleton
type(singleton) # tuple

singleton1 = ("hello")
singleton1
type(singleton1) # str

# single format: tuple[index]
# index : 0  ~  len(tuple)-1
# index: -len(tuple)  ~  -1
f= (2,3,4,5)
f[0]
f[-1] # 索引 -1 表示倒數第1個元素
f[-2]
f[len(f)-1]

# slice format: tuple [start:end ]. Items from start to (end -1)
t=((1,2), (2,"Hi"), (3,"RWEPA"), 2+3j, 6E23)
t[2]
t[:3]
t[3:]
t[-1]
t[-3:]

# tuple 長度
len(t) # 5

# tuple 建構子
# 使用 tuple(( ... )) 或 tuple([ ... ]) 
employeeGender = tuple(("男", "女", "女"))
employeeGender

# tuple unpacking - 將元素指派至變數
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# TRY: green, yellow, red = fruits

# tuple unpacking - 使用萬用字元*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

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

# tuple - join 結合
tuple1 = ("台北", "台中", "高雄")
tuple2 = ("男", "女", "女")
tuple3 = tuple1 + tuple2
print(tuple3)

# tuple - 重複
tuple1*3
3*tuple1

# count 次數統計
tuple = ("男", "女", "女", "男", "女")
tuple.count("男") # 2
tuple.count("女") # 3

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

# 串列 slice format
t=[1, 2, (3,"Hi"), [4,"RWEPA"], 2+3j, 6E7]
t

t[2]
t[:3]
t[3:]
t[-1]
t[-3:]

# 串列長度
len(t)

# list 建構子
# 使用 list(( ... )) 或 list([ ... ])
mylist1 = list(("男", "女", "女"))
mylist1

mylist2 = list(["男", "女", "女"])
mylist2

mylist1 == mylist2

# 串列 unpacking - 將元素指派至變數
fruits = ["apple", "banana", "cherry"]
green, yellow, red = fruits
print(green)
print(yellow)
print(red)
type(green) # str

# 串列 unpacking - 使用萬用字元*
fruits = ["apple", "banana", "cherry", "strawberry", "raspberry"]
green, yellow, *red = fruits
print(green)
print(yellow)
print(red)
type(green) # str

# 串列 - loop 處理
mylist = [1, 2, 3, [4, 5], ["A", "B", "C"]]
# 練習 loop 方法

# 方法1. list - 取出元素, 使用for
for x in mylist:
  print(x)

# 方法2. list - 取出元素, 使用while
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1

# 方法3. list - 取出元素, 使用指標 range, len
for i in range(len(mylist)):
  print(mylist[i])

# 方法4. list - 取出元素, 使用串列包含法 (List Comprehension)
[print(x) for x in mylist]

# 串列包含法應用

# for 資料篩選-包括字母 a
codes = ["Python", "R", "SQL", "Julia", ".NET", "Java", "JavaScript"]
newlist = []
for x in codes:
  if "a" in x:
    newlist.append(x)
print(newlist)

# 串列包含法應用1
# 亦可用於序列, 集合, 字典等可反覆運算物件(可迭代物件, iterable object)
codes = ["Python", "R", "SQL", "Julia", ".NET", "Java", "JavaScript"]
newlist = [x for x in codes if "a" in x]
print(newlist)

# 串列包含法應用2
newlist = [x.upper() for x in codes]
print(newlist)

codes.upper() # AttributeError: 'list' object has no attribute 'upper'

# 串列包含法應用3
newlist = ['RWEPA' for x in codes]
print(newlist)

# 串列 join 結合
e = a + b  # Join two lists
e

# 串列 repeat 重複
f1 = a*3    # repeat lists
f1

f2 = 3*a
f2

# 串列排序-預設為遞增排序,英文字母先大寫,再小寫
codes = ["python", "R", "SQL", "Julia", ".NET", "java", "JavaScript"]
codes.sort()
print(codes)

# 串列排序-先全部小寫,再排序
codes = ["python", "R", "SQL", "Julia", ".NET", "java", "JavaScript"]
codes.sort(key = str.lower)
print(codes)

# 串列排序-遞減排序
codes = ["python", "R", "SQL", "Julia", ".NET", "java", "JavaScript"]
codes.sort(reverse =True)
print(codes)

# 串列反序
codes = ["python", "R", "SQL", "Julia", ".NET", "java", "JavaScript"]
codes.reverse()
print(codes)

# 串列複製,等號會建立參考物件
a = [1, 2, 3]
a
b = a
b[0] = 999 # 修改b,亦會修改a
b
a # a已經更新

# 串列複製-使用 copy
a = [1, 2, 3]
b = a.copy()
b
b[0] = 999
b
a # a保持不變

# 串列複製-使用 list
a = [1, 2, 3]
c = list(a)
c
c[0] = 123
c
a # a保持不變

# 附加元素 append
a = [1, 2, 3]
a.append(['BigData', 'SQL']) # 新增1個元素
a
a.append('2021/8/14')
a

# 延伸元素 extend
a.extend(['Python', 'R', "Julia"]) # 新增一個串列
a

# 延伸元素 extend - 加入tuple,list,set,dict
a = [1, 2, 3]
a.extend(('4', '5', 'RWEPA')) # 延伸一個序列
a

a.extend({'8', '8', '10'}) # 延伸一個集合
a

a.extend({'a':'R', 'b':'Python'}) # 延伸一個字典-ONLY KEY, NO VALUE
a

# 串列 – insert

# 插入元素
a = list(range(5))
a
a.insert(2, 999) # 在指標為2的位置,插入新元素
a

# 串列 – remove, pop, del

# 刪除指定元素
a.remove(999)
a

# 刪除指定指標元素
a.pop(1)
a

# 刪除指定指標元素
del a[1]
a

# 刪除第一個元素
a.pop(0)
a

# 刪除最後一個元素
a.pop()
a

# 清空物件元素,物件仍存在記憶體
a.clear()
a

# 刪除物件,物件不存在記憶體
del a
print(a) # NameError: name 'a' is not defined

# 串列 - zip 應用
a = ("x1", "x2", "x3")
b = ("y1", "y2", "y3")
c = (1, 2, 3)

x = zip(a, b, c)
x
list(x)

# 顯示方法
print(dir(list))

# 實作練習4
# 如何顯示不以 __ 開始串列方法的總個數 11

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

# 使用 myset 練習集合 - loop 方法
myset = {"台北市", "新北市", "桃園市", "台中市", "高雄市"}
myset

# 集合新增元素 add, 因為集合是unordered, 不一定新增在最後一個
myset = {"台北市", "新北市", "桃園市", "台中市", "高雄市"}
myset.add("台南市")
myset

# 集合新增集合
myset.update({"澎湖", "金門"})
myset

# 刪除指定元素
myset.remove("澎湖")
myset

# 清空物件兀素,物件仍存在記憶體
myset.clear()
myset

# 刪除物件,物件不存在記憶體
del myset
myset # NameError: name 'myset' is not defined

# 集合運算
x = {1,2,3,4,5}
y = {1,3,5,7}

x & y # {1, 3, 5} # 交集

x.intersection(y) # 交集

x | y # {1, 2, 3, 4, 5, 7} # 聯集

x.union(y) # 聯集

x ^ y # {2, 4, 7} # XOR 互斥

x - y # 差集

x.difference(y) # 差集

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

# 字典存取元素
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

# dict 刪除元素 - pop
b.pop("shell")
print(b)

# dict 刪除元素 - del
del b["login"]
print(b)

# dict 清空整個物件 - clear
b.clear()
b

# dict 刪除整個物件 -del
del b
b

# dict - items 物件, 回傳 [(key1,value1), (key2,value2,...)]
# 回傳 list[(序列1), (序列2), ...]
b = {
     "uid": 168, 
     "login": "marvelous", 
     "name" : 'Alan Lee',
     "shell": "/bin/sh"
     }
b
x = b.items()
print(x)

# 檢查 key 是否存在
# AttributeError: 'dict' object has no attribute 'has_key'
# 早期版本使用 has_key
if b.has_key("uid"):
	d = b["uid"]
else:
	d = None

# 使用 in
if "uid" in b:   # v3.x 直接使用 in
    d = b["uid"]
else:
    d = None
print(d)

# 使用 get
d = b.get("uid", None) # 較簡潔
print(d)

# dict - loop 處理
mydict = {
    "uid": 168, 
    "login": "marvelous", 
    "name" : 'Alan Lee'
    }
mydict

# for - 回傳 keys
for x in mydict:
    print(x)
    
# for - 使用 keys
for x in mydict.keys():
    print(x)

# for - 回傳 values
for x in mydict:
    print(mydict[x])

# for - 使用 values()
for x in mydict.values():
    print(x)

# for - 回傳 (key, value) 使用 items()
for x,y  in mydict.items():
    print(x, y)

# 字典複製-使用 copy
mydict = {
    "uid": 168, 
    "login": "marvelous", 
    "name" : 'Alan Lee'
    }
mydict

mydict2 = mydict.copy()
print(mydict2)

# 字典複製-使用 dict
mydict3 = dict(mydict)
print(mydict3)

mydict2 == mydict3 # True

# 巢狀字典 (Nested Dictionaries)

# 方法1 一次建立一個巢狀字典
mycodes = {
    "code1" : {
         "name" : "Fortran77",
         "year" : 1977
         },
    "code2" : {
        "name" : "Python",
        "year" : 1991
        },
    "code3" : {
        "name" : "R",
        "year" : 2000
        }
    }

mycodes

# 方法2 建立三個字典,再合併為一項字典
mycode1 = {
    "name" : "Fortran77",
    "year" : 1977
    }

mycode2 = {
    "name" : "Python",
    "year" : 1991
    }

mycode3 = {
    "name" : "R",
    "year" : 2000
    }

mycodes2 = {
  "程式1" : mycode1,
  "程式2" : mycode2,
  "程式3" : mycode3
}

mycodes2

# 實作練習
# 將 list 轉換為 dictionary
# 輸入: lst = ['a', 1, 'b', 2, 'c', 3]
# 結果: {'a': 1, 'b': 2, 'c': 3}
# 技巧: 使用 for loop

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

# 實作練習
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
