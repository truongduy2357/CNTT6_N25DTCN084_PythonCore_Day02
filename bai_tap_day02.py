# Dataset orders:
orders = [
    {"id": "DH01", "name": "iPhone 15 Pro Max", "price": 32000000},
    {"id": "DH02", "name": "Tai nghe AirPods Pro", "price": 5500000},
    {"id": "DH03", "name": "MacBook Pro M3 Max", "price": 65000000},
    {"id": "DH04", "name": "Chuot khong day", "price": 450000},
    {"id": "DH05", "name": "Samsung Galaxy S24", "price": 22000000}
]

# Bài 1
total_revenue = 0
vip_count = 0
max_order = orders[0]
min_order = orders[0]
is_suspicious = False

for order in orders:
    total_revenue += order["price"]
    if order["price"] >= 15000000:
        vip_count += 1

    if order["price"] > max_order["price"]:
            max_order = order
    
    if order["price"] < min_order["price"]:
        min_order = order

print("Bài 1")
print(f"Tổng doanh thu: {total_revenue:,} VNĐ")
print(f"Số đơn hàng VIP (>= 15tr): {vip_count} đơn")
print(f"Đơn hàng giá trị CAO NHẤT: {max_order["id"]} - {max_order["name"]} ({max_order["price"]:,} VND)")
print(f"Đơn hàng giá trị THẤP NHẤT: {min_order["id"]} - {min_order["name"]} ({min_order["price"]:,} VND)")
for order in orders:
    if order["price"] > 50000000:
        is_suspicious = True
        print(f"CẢNH BÁO RỦI RO: Phát hiện đơn {order["id"]} có giá trị {order["price"]:,} > 50tr!")
print(f"KẾT LUẬN CẮM CỜ: Cờ is_suspicious = {is_suspicious}")

# Bài 2
print("\nBài 2")
id = input("Nhập mã sinh viên: ").strip()
name = input("Nhập họ tên sinh viên: ").strip()
email = input("Nhập email: ").strip().lower()
phone = input("Nhập số điện thoại: ").strip()
error = []

if email.count("@") != 1:
    error.append("email không chứa 1 kí tự @")
if not email.endswith((".com", ".edu.vn")):
    error.append("email không kết thúc bằng '.com' hoặc '.edu.vn'")
if not phone.isdigit():
    error.append("sdt chứa chữ")
if len(phone) != 10:
    error.append("sdt không đúng 10 chữ số")
if not phone.startswith("0"):
    error.append("sdt không bắt đầu bằng 0")

print(f"[{id}] {name} | Email: {email} | SDT: {phone} "
    f"-> {"HỒ SƠ HỢP LỆ" if error == [] else f"KHÔNG HỢP LỆ ({", ".join(error)})"}")
