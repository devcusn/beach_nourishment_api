from flask import Flask
from services.wave_height import WaveHeight
from services.wave_height_ml import WaveHeightML
from services.closure_depth import ClosureDepth
app = Flask(__name__)


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


@app.route('/api/clouse_depth')
def closure_depth():
    closureDepth = ClosureDepth()
    return closureDepth.getClosureDepth(23, 23)
