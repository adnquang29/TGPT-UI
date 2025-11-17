from flask import Flask, render_template, request, jsonify
import subprocess
import re

app = Flask(__name__)

def clean_output(text):
    """Hàm làm sạch dữ liệu triệt để và thay thế tên"""
    # 1. Xóa mã ANSI (màu sắc, di chuyển con trỏ...)
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    text = ansi_escape.sub('', text)
    
    text = re.sub(r'(?i)Phind', 'adnquang29', text)
    
    # 2. Tách thành từng dòng để xử lý rác hệ thống
    lines = text.split('\n')
    
    clean_lines = []
    for line in lines:
        # Nếu dòng chứa chữ Loading hoặc các ký tự braille -> Bỏ qua
        if "Loading" in line or any(c in line for c in "⣾⣽⣻⢿⡿⣟⣯⣷"):
            continue
        clean_lines.append(line)
    
    # 3. Gộp lại
    return "\n".join(clean_lines).strip()

def is_vietnamese(text):
    """
    Kiểm tra xem chuỗi có chứa ký tự đặc biệt của tiếng Việt không.
    """
    vietnamese_chars = "àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸĐ"
    return any(char in vietnamese_chars for char in text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_prompt = data.get('prompt')
    
    if not user_prompt:
        return jsonify({'error': 'Không có nội dung'}), 400

    try:
        if is_vietnamese(user_prompt):
            # Nếu phát hiện tiếng Việt
            print("Detect: Vietnamese")
            system_instruction = (
                "\n\n[Instruction: Detect Vietnamese input. Please answer in Vietnamese. "
                "Use Markdown for formatting. Do NOT explain about Markdown syntax.]"
            )
        else:
            # Nếu không (Tiếng Anh hoặc ngôn ngữ khác)
            print("Detect: English/Other")
            system_instruction = (
                "\n\n[Instruction: Please answer in English. "
                "Use Markdown for formatting. Do NOT explain about Markdown syntax.]"
            )
        
        full_prompt = f"{user_prompt} {system_instruction}"
        # ------------------------------------

        cmd = ['./tgpt', '-q', full_prompt]
        
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            encoding='utf-8'
        )
        
        raw_output = result.stdout if result.stdout else result.stderr
        final_response = clean_output(raw_output)

        if not final_response:
             ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
             final_response = ansi_escape.sub('', raw_output)

        return jsonify({'response': final_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
