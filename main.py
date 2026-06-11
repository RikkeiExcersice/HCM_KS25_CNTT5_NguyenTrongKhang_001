list_employees = [
    {
        "id": "NV001",
        "name": "Nguyễn Văn A",
        "salary": 400000,
        "day_work": 25,
        "support_salary": 1500000,
        "total_salary": 11500000,
        "rank": "Khá"
    }
]

def cal_total_salary(new_salary, new_daywork, new_support_salary):
    total_salary = new_salary * new_daywork + new_support_salary
    return total_salary

def ranking_salary(total_salary):
        if total_salary < 9000000:
            new_rank = "Thấp"
        elif total_salary < 15000000:
            new_rank = "Trung bình"
        elif total_salary < 30000000:
            new_rank = "Khá"
        else:
            new_rank = "Cao"
        return new_rank

def show_employees(list_employees):
    print(f'{"Mã NV":<20} | {"Họ tên":<30} | {"Lương ngày":<15} | {"Số ngày công":<20} | {"Phụ cấp":<15} | {"Tổng thu nhập":<15} | {"Phân loại thu nhập":<20}')
    for em in list_employees:
        print("-"*150)
        print(f'{em["id"]:<20} | {em["name"]:<30} | {em["salary"]:<15} | {em["day_work"]:<20} | {em["support_salary"]:<15} | {em["total_salary"]:<15} | {em["rank"]:<20}')
        print("-"*150)

def insert_employees(list_employees):
    new_id = input("Mời bạn nhập id cần thêm: ").upper().strip()
    for em in list_employees:
        if em["id"] == new_id:
            print("Nhân viên đã tồn tại")
            return
        try:
            new_name = input("Mời bạn nhập tên nhân viên mới: ").strip()
            new_salary = int(input("Mời bạn nhập lương cho nhân viên: "))
            new_daywork = int(input("Mời bạn nhập số ngày công: "))
            new_support_salary = int(input("Mời bạn nhập lương phụ cấp: "))
            if new_name == '' or new_salary < 0 or new_daywork < 0 or new_support_salary < 0:
                raise ValueError
            new_total_salary = cal_total_salary(new_salary, new_daywork, new_support_salary)
            new_rank = ranking_salary(new_total_salary)
            list_employees.append(
                {
                    "id": new_id,
                    "name": new_name,
                    "salary": new_salary,
                    "day_work": new_daywork,
                    "support_salary": new_support_salary,
                    "total_salary": new_total_salary,
                    "rank": new_rank,

                }
            )
            print("Thêm thành công")
            return
        except ValueError:
            print("Mời bạn nhập lại !")

def update_infor(list_employees):
    search_id = input(print("Mời bạn nhập id nhân viên cần chỉnh sửa: ")).upper().strip()
    for em in list_employees:
        if em["id"] == search_id:
            try:
                new_salary = int(input("Mời bạn nhập lương cho nhân viên: "))
                new_daywork = int(input("Mời bạn nhập số ngày công: "))
                new_support_salary = int(input("Mời bạn nhập lương phụ cấp: "))
                em["salary"] = new_salary
                em["day_work"] = new_daywork
                em["support_salary"] = new_support_salary
                new_total_salary = cal_total_salary(new_salary, new_daywork, new_support_salary)
                new_rank = ranking_salary(new_total_salary)
                if new_salary < 0 or new_daywork < 0 or new_support_salary < 0:
                    raise ValueError
                em["total_salary"] = new_total_salary
                em["rank"] = new_rank
                print("Chỉnh sửa thành công")
                return
            except ValueError:
                print("Mời bạn nhập lại !")
    else: 
        print("Mã nhân viên không tồn tại !")
        return


def find_emp(list_employees):
    search_id = input("Mời bạn nhập id người cần tìm: ").upper().strip()
    for em in list_employees:
        if em["id"] == search_id:
            print(f'{"Mã NV":<20} | {"Họ tên":<30} | {"Lương ngày":<15} | {"Số ngày công":<20} | {"Phụ cấp":<15} | {"Tổng thu nhập":<15} | {"Phân loại thu nhập":<20}')
            print("-"*150)
            print(f'{em["id"]:<20} | {em["name"]:<30} | {em["salary"]:<15} | {em["day_work"]:<20} | {em["support_salary"]:<15} | {em["total_salary"]:<15} | {em["rank"]:<20}')
            print("-"*150)
            return
    else:
        print("Không có id !")
        return
    
def count_ranking(list_employees):
    count_excellent = 0
    count_good = 0
    count_medium = 0
    count_low = 0
    for em in list_employees:
        if em["rank"] == "Cao":
            count_excellent += 1
        elif em["rank"] == "Khá":
            count_good += 1
        elif em["rank"] == "Trung bình":
            count_medium += 1
        else: 
            count_low += 1

    print(f"""
Số lượng nhân viên giỏi: {count_excellent}
Số lượng nhân viên khá: {count_good}
Số lượng nhân viên trung bình: {count_medium}
Số lượng nhân viên thấp: {count_low}""")
def main():
    while True:
        print("Hệ thống quản lí nhân sự".center(30,'-'))
        print('''1. Hiển thị danh sách nhân viên
2. Tiếp nhận nhân viên mới
3. Cập nhật thông tin và ngày công
4. Xóa nhân viên 
5. Tìm kiếm nhân viên
6. Thống kê quỹ lương và nhân sự
7. Phân loại thu nhập tự động 
8. Thoát chương trình
''')
        try:
            choice = input("Mời bạn nhập lựa chọn: ")
        except ValueError:
            print("Mời bạn nhập lại !")

        match choice:
            case "1":
                show_employees(list_employees)
            case "2":
                insert_employees(list_employees)
            case "3":
                update_infor(list_employees)
            case "4":
                pass
            case "5":
                find_emp(list_employees)
            case "6":
                count_ranking(list_employees)
            case "7":
                pass
            case "8":
                print("Đã thoát chương trình...")
                break
            case _:
                print("Mời bạn nhập đúng lựa chọn !")
main()