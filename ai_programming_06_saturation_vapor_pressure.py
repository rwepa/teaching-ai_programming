"""
File     : ai_programming_06_saturation_vapor_pressure.py
Title    : AI與程式語言-第6章 saturation vapor pressure
Author   : Ming-Chang Lee
Email    : alan9956@gmail.com
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Encoding : UTF-8
"""

# saturation vapor pressure (飽和水氣壓)
# https://en.wikipedia.org/wiki/Tetens_equation
# https://en.wikipedia.org/wiki/Vapour_pressure_of_water

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams # 載入繪圖參數設定
rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 設定字型
rcParams['axes.unicode_minus'] = False # 設定負號正確顯示

# 範例1
# 飽和水氣壓計算
T = 50
a = 17.27
b = 237.3
es = 0.61078*np.exp(a*T/(T+b))
print(es)

# 範例2
# 飽和水氣壓曲線繪圖
T = np.linspace(-100,100,50)
es_formula = 0.61078*np.exp(a*T/(T+b))
plt.plot(T, es_formula)
plt.xlabel('T (degree Celcius)')
plt.ylabel('es (Pa)')
plt.title('TKU-168-李明昌')
plt.show()
# end
