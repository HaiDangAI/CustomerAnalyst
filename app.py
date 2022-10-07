import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import streamlit as st
from streamlit_echarts import st_echarts
from vega_datasets import data

df1 =  pd.read_csv('df_sample_100ktb_(luy_ke).csv')

sum_tkctotal = df1.groupby('month')['tkc_total'].sum().reset_index()['tkc_total']
sum_topup = df1.groupby('month')['topup'].sum().reset_index()['topup']
sum_data = df1.groupby('month')['data'].sum().reset_index()['data']
sum_data = sum_data/1073741824
sum_tkctotal = sum_tkctotal/1000000
sum_topup = sum_topup/1000000
labels = [str(i) for i in df1.month.unique()]
width = 0.6
fig_height = 9
fig_width = 20

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]+100, 
                 np.round(y[i], 3), 
                 ha = 'center')

fig, ax = plt.subplots(figsize=(fig_width, fig_height))
ax.bar(labels, sum_tkctotal, width, 
       label='Tổng tài khoản chính', 
       color=plt.get_cmap("Pastel1").colors, 
       edgecolor = plt.get_cmap("Set1").colors)
addlabels(labels, sum_tkctotal)
ax.set_xlabel('Tháng')
ax.set_ylabel('Tổng tài khoản chính (Triệu)')
plt.title('Tổng tài khoản chính theo từng tháng')
plt.yticks(np.linspace(0, np.ceil(np.max(sum_tkctotal)), 5))
st.pyplot(fig, clear_figure=True)

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]+10, 
                 np.round(y[i], 3), 
                 ha = 'center')

fig, ax = plt.subplots(figsize=(fig_width, fig_height))
ax.bar(labels, sum_topup, width, 
       label='Tổng topup', 
       color=plt.get_cmap("Pastel1").colors, 
       edgecolor = plt.get_cmap("Set1").colors)
addlabels(labels, sum_topup)
ax.set_xlabel('Tháng')
ax.set_ylabel('Tổng topup')
plt.title('Tổng topup theo từng tháng (Triệu)')
plt.yticks(np.linspace(0, np.ceil(np.max(sum_topup)), 5))
st.pyplot(fig, clear_figure=True)


x = np.arange(len(labels))  # the label locations
width3 = 0.35

fig, ax = plt.subplots(figsize=(fig_width, fig_height))
bar1 = ax.bar(x - width3/2, sum_tkctotal, width3, label='sum_tkctotal', 
                color=plt.get_cmap("Pastel1").colors, 
                edgecolor = plt.get_cmap("Set1").colors)
bar2 = ax.bar(x + width3/2, sum_topup, width3, label='sum_topup',
                color=plt.get_cmap("Pastel1").colors, 
                edgecolor = plt.get_cmap("Set1").colors)


ax.set_title('Scores by group and gender')
ax.bar_label(bar1, padding=3)
ax.bar_label(bar2, padding=3)
ax.set_xlabel('Tháng')
ax.set_ylabel('Tổng tiền (triệu)')
# ax.legend()

fig.tight_layout()

plt.xticks(x ,labels)
plt.yticks(np.linspace(0, np.round(np.max(sum_tkctotal.append(sum_topup))), 5))
st.pyplot(fig, clear_figure=True)


fig, ax = plt.subplots(figsize=(fig_width, fig_height))
ax.plot(labels, sum_tkctotal, 
        color='red', 
        marker='o', 
        markersize=10,
        linewidth=2,
        markerfacecolor=mcolors.CSS4_COLORS['gold'],
        label='data')
ax.plot(labels, sum_topup, 
        color='red', 
        marker='o', 
        markersize=10,
        linewidth=2,
        markerfacecolor=mcolors.CSS4_COLORS['violet'],
        label='data')
for xitem,yitem in np.nditer([labels,sum_tkctotal]):
    etiqueta = "{:.3f}".format(np.round(yitem/1e10, 3))
    plt.annotate(etiqueta, (xitem,yitem), textcoords="offset points",xytext=(0,10),ha="center")
for xitem,yitem in np.nditer([labels,sum_topup]):
    etiqueta = "{:.3f}".format(np.round(yitem/1e10, 3))
    plt.annotate(etiqueta, (xitem,yitem), textcoords="offset points",xytext=(0,10),ha="center")
ax.set_title('Tổng lượng data sử dụng theo từng tháng')
ax.set_xlabel('Tháng')
ax.set_ylabel('Tổng lượng data sử dụng')
ax.set_title('Tổng lượng tài khoản chính và topup biến thiên theo từng tháng')
ax.legend()
ax.grid(True)
st.pyplot(fig, clear_figure=True)

fig, ax = plt.subplots(figsize=(fig_width, fig_height))
ax.plot(labels, sum_data, 
        color='red', 
        marker='o', 
        markersize=10,
        linewidth=2,
        markerfacecolor=mcolors.CSS4_COLORS['gold'],
        label='data')
for xitem,yitem in np.nditer([labels,sum_data]):
    etiqueta = "{:.3f}".format(np.round(yitem, 3))
    plt.annotate(etiqueta, (xitem,yitem), textcoords="offset points",xytext=(0,10),ha="center")

ax.set_title('Tổng lượng data sử dụng theo từng tháng')
ax.set_xlabel('Tháng')
ax.set_ylabel('Tổng lượng data sử dụng (GB)')
ax.legend()
ax.grid(True)
st.pyplot(fig, clear_figure=True)


