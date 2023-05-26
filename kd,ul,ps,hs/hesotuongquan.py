import pandas as pd
import matplotlib.pyplot as plt


# Đọc dữ liệu từ file Excel
# df=pd.read_excel('E:\\data\\PTDL\\ds_salaries.xlsx')

# # Hiển thị dữ liệu
# print(df)


# # bài toán tính hệ số tương quan giữa lương và lương bằng USD, lấy dữ liệu trong khoảng từ hàng1-100
# # Tính toán hệ số tương quan trong khoảng từ 1 đến 100
# data_subset = df.iloc[0:100]
# correlation = data_subset['salary'].corr(data_subset['salary_in_usd'])


# # correlation = df['salary'].corr(df['salary_in_usd'])

# print("Hệ số tương quan:", correlation)
tweets=[25,11800,99,1934,199,2539,4334,952,3245,2468]
follower=[7194,43400000,324000,2330000,39000,189000,639000,688000,2690000,110000]
print(len(tweets),len(follower))
# Vẽ biểu đồ
plt.scatter(x=tweets, y=follower, color='blue',)

plt.xlabel('Lượt bài đăng')
plt.ylabel('Số lượng người theo dõi')
plt.title('Biểu đồ tương quan giữa số người theo dõi và số bài đăng')
plt.legend()
plt.show()