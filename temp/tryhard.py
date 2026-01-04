def chinh_sua_diem(d_thuong_xuyen, d_giua_ky, d_cuoi_ky):
    print("--- CHỌN LOẠI ĐIỂM CẦN SỬA ---")
    print("1. Điểm Thường xuyên")
    print("2. Điểm Giữa kỳ")
    print("3. Điểm Cuối kỳ")
    
    loai = input("Nhập lựa chọn của bạn (1-3):")
    
    
    if loai == '1':
        d_hien_tai = d_thuong_xuyen
        ten_loai = "Thường xuyên"
    elif loai == '2':
        d_hien_tai = d_giua_ky
        ten_loai = "Giữa kỳ"
    elif loai == '3':
        d_hien_tai = d_cuoi_ky
        ten_loai = "Cuối kỳ"
    else:
        print("Lựa chọn không hợp lệ!")
        return

    print(f"\nĐang thao tác với: Điểm {ten_loai}")
    print(f"Danh sách hiện tại: {d_hien_tai}")
    if d_hien_tai == d_giua_ky or d_hien_tai == d_cuoi_ky:
        new_score = input('Điểm mới:')
        while new_score.isdigit() == False and new_score > 10:
            new_score = input('Nhập số:')
        new_score = float(new_score)
        d_hien_tai[0] = new_score
    else:
        print("\n--- CHỌN CHẾ ĐỘ SỬA ---")
        print("1. Sửa 1 đầu điểm cụ thể")
        print("2. Sửa lại tất cả đầu điểm")
        mode = input("Nhập lựa chọn (1 hoặc 2): ")

        if mode == '1':
            try:
            # Hiển thị cho người dùng từ 1 đến độ dài list
                vi_tri_nhap = int(input(f"Nhập vị trí muốn sửa (từ 1 đến {len(d_hien_tai)}): "))
                index_thuc = vi_tri_nhap - 1 
                if 0 <= index_thuc < len(d_hien_tai):
                    diem_moi = float(input(f"Nhập điểm mới cho vị trí số {vi_tri_nhap}: "))
                    while diem_moi > 10:
                        diem_moi = float(input('Nhập lại điểm:'))
                    d_hien_tai[index_thuc] = diem_moi
                else:
                    print(f"Lỗi: Vị trí {vi_tri_nhap} không tồn tại trong danh sách!")
            except ValueError:
                print("Lỗi: Vui lòng nhập số hợp lệ.")

        elif mode == '2':
            smaller_equal_10 = False
            try:
                chuoi_nhap = input("Nhập tất cả điểm mới trên cùng 1 dòng, cách nhau bởi dấu cách: ")
                list_moi = [float(x) for x in chuoi_nhap.split()]
                while len(list_moi) != 3:
                    chuoi_nhap = input("Nhập tất cả điểm mới trên cùng 1 dòng, cách nhau bởi dấu cách: ")
                    list_moi = [float(x) for x in chuoi_nhap.split()]
                while smaller_equal_10 == False:
                    if any(x > 10 for x in list_moi):
                        chuoi_nhap = input("Nhập tất cả điểm mới trên cùng 1 dòng, cách nhau bởi dấu cách: ")
                        list_moi = [float(x) for x in chuoi_nhap.split()]
                    else:
                        smaller_equal_10 = True
                d_hien_tai[:] = list_moi
                print("Đã thay thế toàn bộ danh sách điểm!")
            except ValueError:
                print("Lỗi: Dữ liệu nhập vào không phải là số.")
        else:
            print("Lựa chọn không hợp lệ!")

    return d_thuong_xuyen, d_giua_ky, d_cuoi_ky

thuongxuyen = [9.0, 10.0, 7.3]
giuaky = [8.5]
cuoiky = [9.6]
print(chinh_sua_diem(thuongxuyen, giuaky, cuoiky))
