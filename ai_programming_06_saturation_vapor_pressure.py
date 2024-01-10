"""
File     : ai_programming_06_saturation_vapor_pressure.py
Title    : AI與程式語言-第6章 saturation vapor pressure (飽和水氣壓曲線)
Author   : Ming-Chang Lee
Email    : alan9956@gmail.com
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Encoding : UTF-8
"""

import numpy as np
import matplotlib.pyplot as plt

# 範例1
T = 50
es = 611*np.exp(17.27*T/(237.3+T))
print(es)

# 範例2
T = np.linspace(-100,100,50)
es = 611*np.exp(17.27*T/(237.3+T))

plt.plot(T,es)
plt.xlabel('T (degree Celcius)')
plt.ylabel('es (Pa)')
plt.title('tku-LEE Ming-Chang')
# end
