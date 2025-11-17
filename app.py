from flask import Flask, render_template, request, jsonify
import subprocess
import re

app = Flask(__name__)

def clean_output(text):
    """Hàm làm sạch dữ liệu triệt để"""
    # 1. Xóa mã ANSI (màu sắc, di chuyển con trỏ...)
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    text = ansi_escape.sub('', text)
    
    # 2. Tách thành từng dòng để xử lý
    lines = text.split('\n')
    
    # 3. Chỉ giữ lại những dòng KHÔNG chứa chữ "Loading" và ký tự xoay
    clean_lines = []
    for line in lines:
        # Nếu dòng chứa chữ Loading hoặc các ký tự braille -> Bỏ qua
        if "Loading" in line or any(c in line for c in "⣾⣽⣻⢿⡿⣟⣯⣷"):
            continue
        clean_lines.append(line)
    
    # 4. Gộp lại và xóa khoảng trắng thừa đầu đuôi
    return "\n".join(clean_lines).strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({'error': 'Không có nội dung'}), 400

    try:
        # Thử thêm '-q' (quiet mode) để tắt animation ngay từ nguồn
        # Nếu tgpt bản cũ không hiểu '-q', nó có thể báo lỗi, nên ta dùng try/catch ở output
        cmd = ['./tgpt', '-q', prompt]
        
        # Lưu ý: Nếu lệnh trên lỗi do không hiểu '-q', hãy đổi thành: ['./tgpt', prompt]
        
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            encoding='utf-8'
        )
        
        # Lấy output dù lệnh thành công hay thất bại (đôi khi tgpt trả về stderr vẫn là text)
        raw_output = result.stdout if result.stdout else result.stderr
        
        # Gọi hàm làm sạch "siêu cấp"
        final_response = clean_output(raw_output)

        # Kiểm tra nếu kết quả rỗng (do lọc quá tay hoặc lỗi)
        if not final_response:
             # Fallback: thử trả về raw nhưng đã strip ANSI
             ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
             final_response = ansi_escape.sub('', raw_output)

        return jsonify({'response': final_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
