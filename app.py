from flask import Flask, request

from tests.wave_height import WaveHeight
from tests.wave_height_ml import WaveHeightML
from services.closure_depth import ClosureDepth
from services.volume import Volume
from services.revetment import Revetment
from services.territory import Territory
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
    data = request.get_json()
    wave_height = float(data['wave_height'])
    wave_period = float(data['wave_period'])
    D = float(data['D'])
    dfifthy = float(data['dfifthy'])
    rho = float(data['rho'])
    total_length = float(data['total_length'])
    length_of_beach = float(data['length_of_beach'])
    revetment_data = float(data['revetment'])
    # ClosureDepth class
    closureDepth = ClosureDepth({
        "wave_height": wave_height,
        "wave_period": wave_period,
        "D": D,
        "dfifthy": dfifthy,
        "rho": rho,
    })
    res = closureDepth.res()
    coords = [[
        [0, 0, 0],
        [res['closure_depth_x'], 0, 0],
        [0, res['closure_depth'], 0]
    ], [
        [10, 0, 50],
        [res['closure_depth_x'], 0, 50],
        [10, res['closure_depth'], 50]
    ], [
        [30, 0, 120],
        [res['closure_depth_x'], 0, 120],
        [30, res['closure_depth'], 120]
    ],
        [
        [40, 0, 150],
        [res['closure_depth_x'], 0, 150],
        [40, res['closure_depth'], 150]
    ]]

    territory = Territory(
        coords, res['A'], total_length, length_of_beach)
    result = territory.get_territory_matris()

    res['matris'] = result
    res['volume'] = 500
    res['after_errosion'] = 52.44
    res['beach_length'] = length_of_beach
    res['total_length'] = total_length
    res['revetment'] = revetment_data

    revetment = Revetment(revetment_data, res['A'])
    volume = Volume(res['A'], length_of_beach,
                    total_length, res['closure_depth_x'])
    res['revetment_position'] = revetment.get_position_of_revetment()
    res['volume'] = volume.getVolume()
    return {"data": res}
