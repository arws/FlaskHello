from flask import Flask
from flask import jsonify
from flask import request
import pandas as pd
import os

app = Flask(__name__)


class Settings(object):
    index_daybar_url = 'D:\\data\\h5data\\index\\daybar\\byIndex'


class IndexUtil(object):
    d = {
        '000001': '上证指数',
        '000016': '上证50',
        '000300': '沪深300',
        '000852': '中证1000',
        '000905': '中证500',
        '000906': '中证800',
        '399001': '深圳成指',
        '399005': '中小板指',
        '399006': '创业板指',
        '801010': '申万农林牧渔',
        '801020': '申万采掘',
        '801030': '申万化工',
        '801040': '申万钢铁',
        '801050': '申万有色',
        '801080': '申万电子',
        '801110': '申万家用电器',
        '801120': '申万食品饮料',
        '801130': '申万纺织服装',
        '801140': '申万轻工制造',
        '801150': '申万医药生物',
        '801160': '申万公用事业',
        '801170': '申万交通运输',
        '801180': '申万房地产',
        '801200': '申万商业贸易',
        '801210': '申万休闲服务',
        '801230': '申万综合',
        '801710': '申万建筑材料',
        '801720': '申万建筑装饰',
        '801730': '申万电气设备',
        '801740': '申万国防军工',
        '801750': '申万计算机',
        '801760': '申万传媒',
        '801770': '申万通信',
        '801780': '申万银行',
        '801790': '申万非银金融',
        '801880': '申万汽车',
        '801890': '申万机械设备'
    }

    f = {
        '上证指数': '000001',
        '上证50': '000016',
        '沪深300': '000300',
        '中证1000': '000852',
        '中证500': '000905',
        '中证800': '000906',
        '深圳成指': '399001',
        '中小板指': '399005',
        '创业板指': '399006',
        '申万农林牧渔': '801010',
        '申万采掘': '801020',
        '申万化工': '801030',
        '申万钢铁': '801040',
        '申万有色': '801050',
        '申万电子': '801080',
        '申万家用电器': '801110',
        '申万食品饮料': '801120',
        '申万纺织服装': '801130',
        '申万轻工制造': '801140',
        '申万医药生物': '801150',
        '申万公用事业': '801160',
        '申万交通运输': '801170',
        '申万房地产': '801180',
        '申万商业贸易': '801200',
        '申万休闲服务': '801210',
        '申万综合': '801230',
        '申万建筑材料': '801710',
        '申万建筑装饰': '801720',
        '申万电气设备': '801730',
        '申万国防军工': '801740',
        '申万计算机': '801750',
        '申万传媒': '801760',
        '申万通信': '801770',
        '申万银行': '801780',
        '申万非银金融': '801790',
        '申万汽车': '801880',
        '申万机械设备': '801890'
    }

    @classmethod
    def codeToName(cls, code):
        try:
            return cls.d[code]
        except KeyError:
            return code

    @classmethod
    def nameTocode(cls, name):
        try:
            return cls.f[name]
        except KeyError:
            return name


@app.route('/data/macro', methods=['GET'])
def getMarco():
    data = []

    df = pd.read_excel('D:\SourceCode\python\FlaskDataApi\marco-quarter.xlsx')
    x = [s.strftime('%Y%m') for s in df.index]
    for col in df.columns.values:
        value = [round(x, 4) for x in df[col].values.tolist()]
        data.append({'name': col, 'x': x, 'y': value, 'active': True})
    return jsonify({'data': data})


@app.route('/data/indexlist', methods=['GET', 'POST'])
def getIndexList():
    data = []
    list = [IndexUtil.nameTocode(x) for x in request.args.getlist(key='codes')]
    url = Settings.index_daybar_url
    df_dapan = pd.read_csv(os.path.join(url, '000001.csv'), index_col=['Date'], usecols=['Date', 'Close'])
    for code in list:
        file_name = os.path.join(url, code + '.csv')
        df = pd.read_csv(file_name, index_col=['Date'], usecols=['Date', 'Close'])
        df_dapan[code] = df['Close']
        df_dapan.fillna(method='ffill', inplace=True)
        df_dapan.fillna(method='bfill', inplace=True)
        data.append({'name': IndexUtil.codeToName(code), 'x': [str(s) for s in df_dapan.index.values.tolist()],
                     'y': df_dapan[code].tolist(), 'active': True})
    return jsonify({'data': data})


@app.route('/data/pig', methods=['GET'])
def getPig():
    data = []

    df = pd.read_excel('D:\SourceCode\python\FlaskDataApi\pig.xls', index_col=[0])
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)
    x = [s.strftime('%Y%m%d') for s in df.index]
    for col in df.columns.values:
        value = [round(x, 4) for x in df[col].values.tolist()]
        data.append({'name': col, 'x': x, 'y': value})
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run()
