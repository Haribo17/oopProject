from flask import Flask, request

app = Flask(__name__)

@app.route('/leak', methods=['POST'])
def leak():
    data = request.json
    print("[🔥 유출된 데이터]", data.get("leak"))  # 유출된 문장 출력
    return '', 200

if __name__ == '__main__':
    app.run(port=5050)