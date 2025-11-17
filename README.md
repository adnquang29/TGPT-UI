# TGPT Web UI

Giao diện web cho (Terminal GPT).  
Dự án này cung cấp giao diện chat phong cách Messenger, chạy trực tiếp trên máy tính cá nhân hoặc VPS mà không cần API Key trả phí.

## Tính năng

- **Không cần API Key:** Hoạt động dựa trên `tgpt`.
- **Giao diện Messenger:** Bong bóng chat xanh/xám, thân thiện.
- **Chế độ Sáng/Tối (Dark Mode):** Chuyển đổi nhanh, tự động lưu cấu hình.
- **Responsive:** Hiển thị tối ưu trên cả máy tính và điện thoại di động.
- **Output sạch:** Tự động lọc bỏ các ký tự loading/animation thừa từ dòng lệnh.

## Cài đặt

### 1. Tải mã nguồn
```bash
git clone https://github.com/adnquang29/TGPT-UI.git
cd TGPT-UI
````

### 2\. Chuẩn bị `tgpt`

Hãy đảm bảo bạn đã có file thực thi `tgpt` nằm ngay trong thư mục gốc của dự án này (ngang hàng với file `app.py`).

### 3\. Cài đặt thư viện

Khuyên dùng môi trường ảo (virtual environment):

```bash
python3 -m venv venv
source venv/bin/activate  # Trên Windows dùng: venv\Scripts\activate
pip install flask
```

## Chạy ứng dụng

Khởi động server với lệnh sau (cho phép truy cập từ IP ngoài):

```bash
flask run --host=0.0.0.0
```

### Truy cập

  - **Mặc định:** [http://127.0.0.1:5000](http://127.0.0.1:5000)
  - **IP nội bộ:** Bạn có thể dùng IP LAN của máy (ví dụ: `192.168.1.x:5000`) để truy cập từ điện thoại hoặc máy khác.

### Các đường dẫn:

  - Truy cập `/` hoặc `/chat-flask` để bắt đầu chat.
  - Truy cập `/chat-flask/results` để xem lịch sử chat (nếu đã cấu hình lưu trữ).

---

## License

Project cá nhân – miễn phí sử dụng.
