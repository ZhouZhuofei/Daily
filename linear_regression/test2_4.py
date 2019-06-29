from __future__ import print_function
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as st
B3 = pd.read_csv('B3.csv')
x = np.array(B3['x1'])
y = np.array(B3['y'])
X = sm.add_constant(x)
Sxx = np.dot(x - np.mean(x), x - np.mean(x))

#最小二乘拟合
r = sm.OLS(y, X).fit()
print(r.summary())


#回归显著性检验

m_l = ols('y ~ x1',data = B3).fit()
table = sm.stats.anova_lm(m_l, typ=1)
print(table)

#当x1 = 275时，里程均值的95%置信区间
x1 = 275
y1 = r.params[0] + r.params[1] * x1

t1 = y1 + st.t.interval(0.95,r.df_resid)[0] * np.sqrt(r.mse_resid*(1/len(y) + (x1 - np.mean(x))**2/Sxx))

t2 = y1 + st.t.interval(0.95,r.df_resid)[1] * np.sqrt(r.mse_resid*(1/len(y) + (x1 - np.mean(x))**2/Sxx))

print((t1,t2))


#汽车里程的95%的置信区间
t3 = y1 + st.t.interval(0.95,r.df_resid)[0] * np.sqrt(r.mse_resid*(1 + 1/len(y) + (x1 - np.mean(x))**2/Sxx))

t4 = y1 + st.t.interval(0.95,r.df_resid)[1] * np.sqrt(r.mse_resid*(1 + 1/len(y) + (x1 - np.mean(x))**2/Sxx))

print((t3,t4))


