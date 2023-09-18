import json

from flask import Flask, request, jsonify

from detect import parse_data

server = Flask(__name__)


@server.route('/process', methods=['POST'])
def on_receive_data():
    try:
        msg = request.get_json()
        print(msg)
    except Exception as e:
        return jsonify({'error': '请求数据失败'}), 400

    global result
    if msg:
        try:
            result = process_data(msg)
        except Exception as e:
            print(e)
            return jsonify({'error': '处理数据失败'}), 666
    if not result:
        result = "error"

    return {"output_path": result}

def process_data(msg):
    data = msg
    print(data)
    save_path = ""
    if data["fileType"] == "IMG_DIR" and data["imageType"] == "JPG":
        input_path = data["filePath"]
        output_path = data['outputPath']
        if output_path:
            save_path = parse_data(input_path, output_path)
        else:
            save_path = parse_data(input_path)
    return save_path

if __name__ == '__main__':
    server.run()