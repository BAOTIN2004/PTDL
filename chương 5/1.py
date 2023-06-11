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
    df=data['company_size'].value_counts()
    lable=df.index.tolist()
    my_colors= ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    plt.pie(df,labels=lable,autopct='%1.1f%%',colors=my_colors)
    plt.title('Tỉ lệ mỗi loại công ty')
    plt.show()

def bieu_do_duong_luong_nam():
    df=data.groupby(['work_year'])['salary_in_usd'].mean()
    years = df.index.tolist()
    plt.title('Biểu lương trung bình năm')
    plt.plot(years,df.values)
    plt.show()


    
def bieu_do_thanh_loai_cty():
    df=data['company_size'].value_counts()
    a=df.index.tolist()
    plt.bar(a,df.values,color='green',width=0.3)
    plt.xlabel('Loại công ty')
    plt.ylabel('Số lượng nhân viên ')
    plt.title('Biểu đồ số lượng nhân viên mỗi loại cty')
    plt.show()
    
def bieu_do_tb_luong_loai_lmvc():
    df=data.groupby(['employment_type'])['salary_in_usd'].mean()
    plt.barh(df.index.tolist(),df,color='orange',height=0.5)
    plt.title('Biểu đồ trung binh lương mỗi loại hình làm việc')
    plt.xlabel('Lương (usd)')
    plt.ylabel('Loại')
    plt.show()

import pandas as pd
import numpy as np
pd.plotting.register_matplotlib_converters()
import seaborn as sns
# data = pd.read_excel("C:\\Users\ADMIN\\quocdan\\ds_salaries.xlsx")#đọc dữ liệu
#print(data)

#print("đếm xem có bao nhiêu giá trị duy nhất trong cột:\n\n", data.nunique())

#print("tóm tắc ngắn gọn các thông tin của dữ liệu \n\n",data.info())

#print("in ta tổng số giá trị thiếu trong mỗi cột của dữ liệu \n\n",data.isna().sum())

#print("in ra tổng số các giá trị duy nhất trong các cột \n",data[['work_year', 'salary']].value_counts())

# - Tính trung bình, trung vị, max, min của mức lương của các công việc 
grouped_data = data.groupby('job_title')['salary'].agg(['mean', 'median', 'max', 'min'])
# In ra bản phân tổ 
#print("bảng phân tổ các loại công việc theo mức lương \n", grouped_data)

def bieu_do_tron_experience_level(): 
   # kích thước của hình
   plt.figure(figsize = (10, 8))
   # tạo biểu đồ tròn thể hiện sự phân phối cấp độ kinh nghiệm
   data['experience_level'].value_counts().plot(kind='pie', autopct='%1.1f%%', cmap='viridis')
   # thêm tiêu đề cho biểu đồ
   plt.title('Bảng phân phối các cấp độ kinh nghiệm')
   plt.show()
   
def bieu_do_duong_mean():
   meanYearlySalary = np.array(data['salary_in_usd'].groupby(data['work_year']).mean())
   plt.xlabel('Năm')
   plt.ylabel('Lương trung bình($)')
   plt.title("Giá trị trung bình mức lương USD qua các năm")
   sns.lineplot(x=['2020', '2021', '2022', '2023'], y=meanYearlySalary)
   plt.show()


def bieu_do_cot_median():
   
   data.groupby('work_year')['salary_in_usd'].median().plot.bar()
   plt.xlabel('Năm')
   plt.ylabel('Giá trị tung vị của lương')
   plt.title('Giá trị trung vị mức lương USD qua các năm ')

   plt.show()


def alltime_top_ten():
   allTimeTopTen = data["job_title"].value_counts().nlargest(10).reset_index()
   sns.barplot(x=allTimeTopTen["job_title"], y=allTimeTopTen["index"])
   plt.title("Top 10 công việc Data Scicence phổ biến nhất")
   plt.xlabel("Số lượng")
   plt.ylabel("Ngành")
   plt.show()

def alltime_top_ten_2023():
   topTen2023 = data[data["work_year"]==2023]["job_title"].value_counts().nlargest(10).reset_index()
   sns.barplot(x=topTen2023["job_title"], y=topTen2023["index"])
   plt.title("Top 10 công việc Data Scicence phổ biến nhất 2023")
   plt.xlabel("Số lượng")
   plt.ylabel("Tên cv")
   plt.show()


def experience_level_vs_work_year():
    # Phân tích năm làm việc và mức độ kinh nghiệm bằng hàm pandas cross-tab
    pd.crosstab(data['work_year'],data['experience_level'], normalize = 'index').plot(kind = 'bar')
    plt.xlabel('Year')
    plt.ylabel('Mật độ xác suất')
    plt.title('Cấp độ kinh nghiệm so với năm làm việc')
    plt.xticks(rotation = 0)
    plt.show()

def bieu_do_remote_ratio():
   sns.histplot(data['remote_ratio'], kde = True)
   plt.xlabel('Remote Ratio')
   plt.ylabel('Mật độ')
   plt.title('Phân phối tỷ lệ từ xa')
   plt.show()

def histogram():
# Create histogram
   sns.histplot(x = 'salary_in_usd', hue = 'experience_level', multiple = 'stack',
               edgecolor = '#cfd0d4', bins = 50, data = data, palette = 'viridis')
   # Customize the title and labels
   plt.grid(alpha = 0.3)
   plt.title('Phân phối tiền lương theo kinh nghiệm qua các năm')
   plt.xlabel('Lương($)')
   plt.ylabel('Số lượng')
   # Display the plot
   plt.show()

def tuong_quang_experience_level_company_size():
   # Tạo một bảng chéo của hai cột
    cross_tab = pd.crosstab(data['experience_level'], data['company_size'])
    # Tạo một bản đồ nhiệt bằng cách sử dụng dữ liệu bảng chéo
    plt.figure(figsize=(10, 8))
    sns.heatmap(cross_tab, annot=True, fmt="d", cmap='Blues')
    plt.xlabel('Quy mô công ')
    plt.ylabel('Kinh nghiệm')
    plt.title('Mối quan hệ giữa Cấp độ kinh nghiệm và Quy mô công ty')
    plt.show()
ft_sample = data[data['employment_type'] == 'FT']['salary_in_usd']

from scipy.stats import norm
# Kích thước mẫu
n_ft = 3000

# Tính giá trị trung bình mẫu và độ lệch chuẩn mẫu cho FT
mean_ft = ft_sample.mean()
std_ft = ft_sample.std(ddof=1)

# Nhập giá trị tin cậy từ người dùng
confidence_level = float(input("Nhập giá trị tin cậy (từ 0 đến 1): "))

# Giá trị z-score tương ứng với confidence level
z_score_ft = norm.ppf((1 + confidence_level) / 2)

# Tính khoảng tin cậy
margin_of_error_ft = z_score_ft * std_ft / np.sqrt(n_ft)

# ước luoejng khoảng lương trung bình cho loại hình công việc Full time
confidence_interval_ft = (mean_ft - margin_of_error_ft, mean_ft + margin_of_error_ft)

# In kết quả
print("Khoảng tin cậy của giá trị trung bình cho hình thức làm việc toàn thời gian:")
print(confidence_interval_ft)