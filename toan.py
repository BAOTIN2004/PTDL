import pandas as pd
data=pd.read_excel("E:\data\PTDL\ds_salaries.xlsx")
# import matplotlib.pyplot as plt
# x=data['employment_type']
# y=data['salary_in_usd']
# plt.xlabel('Hình thức làm việc')
# plt.ylabel('Lương')
# plt.scatter(x,y,c='red',s=1)
# plt.title('Biểu đồ phân tán hình thức làm việc với lương')
# plt.show()

# import seaborn as sns ,numpy as np
# meanYearlySalary = np.array(data['salary_in_usd'].groupby(data['work_year']).mean())
# plt.xlabel('Năm')
# plt.ylabel('$')
# plt.title("Trung bình lương các năm")
# sns.lineplot(x=['2020', '2021', '2022', '2023'], y=meanYearlySalary)
# plt.show()

# while left_index < len(left) and right_index < len(right):
#         if left[left_index] < right[right_index]:
#             merged.append(left[left_index])
#             left_index += 1
a=0
tb=data['salary_in_usd'].mean()
for i in data['salary_in_usd']:
    a=(i-tb)**2+a
print(a/len(data['salary_in_usd']))