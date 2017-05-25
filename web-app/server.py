from flask import Flask
import random

app = Flask(__name__, static_url_path='/public')

devX = 0.0
devY = 0.0
devZ = 0.0

@app.route("/server/get")
def get_data():
    return 

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/js/main.js")
def js():
    return app.send_static_file('js/main.js')

@app.route("/third-party/vis.custom.js")
def vis():
    return app.send_static_file('third-party/vis.custom.js')

@app.route("/data/driver")
def driver():
    names = ["John", "Peter", "Paul", "Jonah", "Mitchell"]
    name = names[random.randint(0, len(names) - 1)]
    confidence = random.randint(0, 1000) / 10.0
    return '{"name": "' + name + '", "confidence": "' + str(confidence) + '"}'

@app.route("/data/sensor_count")
def sensor_count():
    return '{"count": "' + str(6) + '"}'

@app.route("/data/sensor/<sensor>")
def sensor_data(sensor):
    x = random.randint(0, 20000) / 10000.0 
    y = random.randint(0, 20000) / 10000.0
    z = random.randint(0, 20000) / 10000.0
    return '{"x": "' + str(x) + '", "y": "' + str(y) + '", "z": "' + str(z) + '"}'

@app.route("/data/device/accelerometer/<x>/<y>/<z>")
def device_accelerometer(x, y, z):
    return '{"message": "ok_accel"}'

@app.route("/data/device/gyro/<x>/<y>/<z>")
def device_gyro(x, y, z):
    return '{"message": "ok_gyro"}'
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')