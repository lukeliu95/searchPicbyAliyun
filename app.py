from flask import Flask, render_template, request, jsonify
from searchPic import searchImageByPic  # 更改导入
import io

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    if 'image' not in request.files:
        return jsonify({'error': '没有上传图片'}), 400
    
    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': '没有选择图片'}), 400
    
    try:
        image_bytes = io.BytesIO(image_file.read())
        results = searchImageByPic(image_bytes)
        results_list = results['body']['Auctions']
        pic_names = [item['PicName'] for item in results_list if 'PicName' in item]
        url_prefix = "https://luckybgmoss.oss-cn-hangzhou.aliyuncs.com/imgSearch/"
        # 生成 HTML img 标签
        img_tags = ''.join([f'<div class="image-container"><img src="{url_prefix + pic_name}" alt="{pic_name}" title="{pic_name}" onclick="openImageInModal(\'{url_prefix + pic_name}\')" /></div>\n' for pic_name in pic_names])

        return jsonify(img_tags)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
