from flask import Flask
from flask import jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/macro/index.json', methods=['GET'])
def getMarco():
    data = []

    df = pd.read_excel('E:\code\web\FlaskHello\marco-quarter.xlsx')
    x = [s.strftime('%Y%m') for s in df.index]
    for col in df.columns.values:
        value = [round(x, 2) for x in df[col].values.tolist()]
        data.append({'name': col, 'x': x, 'y': value, 'active': True})
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run()
