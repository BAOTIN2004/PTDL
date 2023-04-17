

# hàm strip() bỏ kí tự xuống dòng
#)
def tinh_toan():
    file=open("E:\\PTDL\\pandas\\hs.csv",mode="r",encoding="utf-8-sig")
    d1=file.readline()
    file_new=open("E:\\PTDL\\pandas\\students_new.csv",mode='w',encoding="utf-8-sig")
    file_new.write(d1.strip()+',Điểm trung bình,Xếp loại\n')
    row=file.readline()
    # lặp hết tất cả các dòn
    while row!='':
        row_list=row.split(',')
        toan=row_list[2]
        van=row_list[3]
        tb=round((float(toan)+float(van))/2,1)
        if tb>=8: rank="Giỏi"
        elif tb<8 and tb>=6.5: rank='Tiên tiến'
        elif tb<4: rank="Yếu"
        else: rank="Trung bình"
        new_row=row.strip()+f',{tb},{rank}\n'
        file_new.write(new_row)
        row=file.readline()
tinh_toan()