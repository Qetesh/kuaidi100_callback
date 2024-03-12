import json

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/kuaidi100/callback', methods=['POST'])
def callback():
    data = request.form['param']
    resultRaw = json.loads(data)
    progressResult = ''
    for i in resultRaw['lastResult']['data']:
        progressResult = progressResult + i['time'] + ' -' + i['context'] + '\n'
    result = f'''快递信息更新通知：
快递单号：{resultRaw['lastResult']['nu']}
快递公司：{resultRaw['lastResult']['com']}
快递状态：{resultRaw['status']}
快递进度：
{progressResult}
  '''
    print(result)

    return jsonify({'result': True, "returnCode": "200", "message": "成功"})


if __name__ == '__main__':
    app.run()
