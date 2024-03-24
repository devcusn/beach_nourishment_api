from flask import Flask, request
from services.territory import Territory
from services.wave_height import WaveHeight
from services.wave_height_ml import WaveHeightML
from services.closure_depth import ClosureDepth
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_api():
    return "<p>Hello, welcome to beach nourishment api</p>"


@app.route("/api/wave_heigh")
def calculateWaveHeight():
    cas = WaveHeight()
    return str(cas.getWaveLength())


@app.route("/api/ml/wave_heigth")
def calculateWaveHeightML():
    whML = WaveHeightML()
    whML.run()
    return str(whML.getResult())


@app.route('/api/closure_depth', methods=['POST'])
def closure_depth():
    # data
    data = request.get_json()
    wave_height = float(data['wave_height'])
    wave_period = float(data['wave_period'])
    D = float(data['D'])
    dfifthy = float(data['dfifthy'])
    rho = float(data['rho'])
    # ClosureDepth class
    closureDepth = ClosureDepth({
        "wave_height": wave_height,
        "wave_period": wave_period,
        "D": D,
        "dfifthy": dfifthy,
        "rho": rho,
    })
    res = closureDepth.res()
    coords = [
        [0, 0, 0],
        [res['x'], 0, 0],
        [0, -1*res['closure_depth'], 0]
    ]

    territory = Territory(coords, res['A'])
    result = territory.get_territory_matris()
    res['matris'] = result
    # return response
    return {"data": res}
