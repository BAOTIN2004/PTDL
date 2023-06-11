import matplotlib.pyplot as plt 
import numpy as np
import math 
import pandas as pd
data=pd.read_excel("E:\data\PTDL\ds_salaries.xlsx")

def bieu_do_phan_to():
    s=data.groupby('experience_level').agg({'salary_in_usd':['min','max','mean','median']})
    # ax = s.plot(kind='line', subplots=True)

    ax = s.plot(kind='line')

    # Chú thích các thông tin trên biểu đồ
    labels = ['Lương thấp nhất', 'Lương cao nhất', 'Lương trung bình', 'Lương trung vị']
    lines, _ = ax.get_legend_handles_labels()
    ax.legend(lines, labels, loc='best')
    plt.title('Mốc lương theo từng loại kinh nghiệm')
    plt.show()
work_year=data['work_year'].unique()
work_year_df={'Năm':work_year }
print(work_year_df)

a=data['experience_level'].value_counts()
print(a)