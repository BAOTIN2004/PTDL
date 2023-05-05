import matplotlib.pyplot as plt 
import numpy as np
import math
import pandas as pd

data = pd.read_excel("E:\data\PTDL\ds_salaries.xlsx")


# experience_level : mức độ kinh nghiệm
# Remote ratio : tỷ lệ làm việc từ xa
# Employment type :loại hình việc làm( full time,part time,contract: kí hợp đồng, freelance:nv tự )
# Salary_currency là đơn vị tiền tệ được sử dụng để thể hiện số tiền lương
# employee_residence: nơi cư trú nhân viên
def bieu_do_tron_loai_cv():
    df=data['employment_type'].value_counts()
    lable=df.index.tolist()
    my_colors= ['green','red','silver','lightblue']
    plt.pie(df,labels=lable,autopct='%1.1f%%',colors=my_colors)
    plt.title('Biểu đồ loại việc làm')
    plt.show()
    
def bieu_do_duong_luong_nam():
    df=data.groupby(['year'])['salary_in_usd'].mean()
    years = df.index.tolist()
    plt.plot(years,df.values)
    plt.show()

df=data.groupby(['company_size'])['salary_in_usd'].sum()
a=years = df.index.tolist()
plt.bar(a,df)
plt.show()
