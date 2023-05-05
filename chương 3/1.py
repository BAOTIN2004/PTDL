# 3.3 Một số đại lượng biểu thị xu hướng trung tâm

# 3.3.1 Giá trị trung bình
import numpy as np
def gia_tri_trung_binh():
    x=[6,3,4,2]
    mean=sum(x)/len(x)
    # hoặc có thể dùng các hàm thư viện numpy
    mean=np.mean(x)
    print(mean)
    x=[6,3,4,2]
    # nếu có dữ liệu trống (nan) thì cần xử lí , vd : x_with_nan=[6,3,4,2,math.nan]

# 3.3.2 Trung bình có trọng số
    # Giá trị trung bình có trọng số , còn được gọi là giá trị trung bình số học có trọng số hoặc trung bình có trọng sốm, là một dàng tổng quát của các fias trị trung bình số học cho phép xác định sự đóng gọp tươg đối của mỗi điểm dữ liệu vào kết quả.
    def tb_trong_so():
            x = [2, 4, 8] 
            w = [0.2, 0.5, 0.3] 
            weighted_mean = np.average(x, weights = w,axis=0) 
            print(weighted_mean)       
# 3.3.3 Median
    # Trung vị mẫu (median) là phần tử giữa của tập dữ liệu đã sắp xếp
    def median():
        x=[2,3,12,1,]
        median=np.median(x)
        print(median)
        
# 3.3.4 Mode
    # Mode là giá trị trong tập dữ liệu xảy ra thường xuyên nhất. Để tìm mode, chúng ta cần sử dụng thư viện statistics
    import statistics 
    def mode():
        x=[2,3,4,1,2,2]
        mode=statistics.mode(x)
        print(mode)
# 3.3.5 

