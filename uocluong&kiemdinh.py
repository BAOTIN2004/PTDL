# Giả thuyết không (H0): Đây là giả thuyết mà chúng ta muốn kiểm tra và bác bỏ nếu có đủ bằng chứng. Nó thường cho rằng không có sự khác biệt, không có mối liên hệ hoặc không có tác động đáng kể giữa các biến hoặc nhóm được so sánh trong bài toán
# Giả thuyết thay thế (H1 hoặc HA): Đây là giả thuyết mà chúng ta mong muốn chứng minh hoặc giả sử rằng có sự khác biệt, mối liên hệ hoặc tác động đáng kể giữa các biến hoặc nhóm được so sánh trong bài toán.

import scipy.stats as stats
import pandas as pd
data=pd.read_excel('E:\\data\\PTDL\\ds_salaries.xlsx')
# Giả sử ta muốn lương trung bình của một ngành nào đó có được 120k($) hay 
a1=data[data['job_title']=='Data Scientist']['salary_in_usd']
# a=data.groupby(['job_title'].['ML Engineer'])['salary_in_usd'].mean()
# kiểm tra t một mẫu
#print(data[data['job_title']=='Data Scientist']['salary_in_usd'].mean())
t1=stats.ttest_1samp(a=a1,popmean=130000)
print(t1)
# alpha là mức rủi ro mà bạn chấp nhận để sai lầm khi từ chối giả thuyết không khi nó đúng. Nó cho biết khả năng mắc phải sai sót kiểu I (false positive), tức là kết luận sai rằng có sự khác biệt khi thực tế không có.
# giá trị thống kê 5.9 > 0 cho thấy lương tb cao hơn 130k
# giá trị p-value gần 0 rất nhỏ nên cta có đủ bằng chứng để bác bỏ giả thuyết giá trị tb luong dự đoán bằng với thực tế
# df :839 số lượng mẫu trong nhóm.

# kiểm định hai mẫu 
# tow sapmle t test sử dụng để kiểm tra giá trị trung bình của hai mẫu có bằng nhau hay không.
a2=data[data['job_title']=='Data Scientist']['salary_in_usd']
a3=data[data['job_title']=='Machine Learning Engineer']['salary_in_usd']
t2=stats.ttest_ind(a=a1,b=a3,equal_var=True)
print(t2)
# giá trị thống kê -3.3 cho thấy trung bình của  scien thấp hơn so với kĩ sư học máy
# giá trị p-value rất nhỏ, đây là xác suất tìm thấy sự biến động trong 2 mẫu dữ liệu với giá trị trung 
