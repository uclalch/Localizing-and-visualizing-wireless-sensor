from flask import Flask, jsonify, request
from datetime import datetime
app = Flask(__name__)

sensors = {
    'acc_x': {'data': None, 'timestamp': None},
    'acc_y': {'data': None, 'timestamp': None},
    'acc_z': {'data': None, 'timestamp': None},
    'gyr_x': {'data': None, 'timestamp': None},
    'gyr_y': {'data': None, 'timestamp': None},
    'gyr_z': {'data': None, 'timestamp': None},
    'phase': {'data': None, 'timestamp': None},
    'capture': {'data': None, 'timestamp': None},
}

@app.route('/data', methods=['GET'])
def get_data():
    global sensors
    return jsonify(sensors)

@app.route('/update', methods=['GET'])
def update_data():
    
    global sensors
    now = datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')

    # Update Accelerometer
    if request.args.get('acc_x'):
        sensors['acc_x']['data'] = float(request.args.get('acc_x'))
        sensors['acc_x']['timestamp'] = now
    if request.args.get('acc_y'):
        sensors['acc_y']['data'] = float(request.args.get('acc_y'))
        sensors['acc_y']['timestamp'] = now
    if request.args.get('acc_z'):
        sensors['acc_z']['data'] = float(request.args.get('acc_z'))
        sensors['acc_z']['timestamp'] = now

    # Update Gyroscope
    if request.args.get('gyr_x'):
        sensors['gyr_x']['data'] = float(request.args.get('gyr_x'))
        sensors['gyr_x']['timestamp'] = now
    if request.args.get('gyr_y'):
        sensors['gyr_y']['data'] = float(request.args.get('gyr_y'))
        sensors['gyr_y']['timestamp'] = now
    if request.args.get('gyr_z'):
        sensors['gyr_z']['data'] = float(request.args.get('gyr_z'))
        sensors['gyr_z']['timestamp'] = now

    # Update USRP Data
    if request.args.get('phase'):
        sensors['phase']['data'] = float(request.args.get('phase'))
        sensors['phase']['timestamp'] = now
    if request.args.get('capture'):
        sensors['capture']['data'] = float(request.args.get('capture'))
        sensors['capture']['timestamp'] = now

    return "SUCCESS"

if __name__ == "__main__":
    app.run()