from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # 处理表单提交
        subscription_text = request.form['subscription_text']
        
        # 将输入框的内容替换到 rss.py 文件中的网页 RSS 订阅地址
        with open('rss.py', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open('rss.py', 'w', encoding='utf-8') as file:
            for line in lines:
                if 'rss_url =' in line:
                    file.write(f'rss_url = "{subscription_text}"\n')
                else:
                    file.write(line)
        
        # 运行 rss.py 文件，并获取输出内容
        output = subprocess.check_output(['python3', 'rss.py']).decode('utf-8')
        
        # 在网页上显示输出内容
        return render_template('index.html', output=output)
    
    # 渲染包含输入框和确定按钮的模板
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12589)
