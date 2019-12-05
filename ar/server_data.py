import requests
from datetime import datetime

class Sensors:
    def __init__(self):
        self.data = None
        self.data_prev = None

    def update(self):
        res = requests.get('http://127.0.0.1:5000/data')
        self.data_prev = self.data
        self.data = res.json()
        
    def time_diff(self, field):
        t1_str = self.data_prev[field]['timestamp']
        t2_str = self.data[field]['timestamp']

        t1 = datetime.strptime(t1_str, '%Y-%m-%d %H:%M:%S.%f')
        t2 = datetime.strptime(t2_str, '%Y-%m-%d %H:%M:%S.%f')

        diff_obj = t2 - t1
        return diff_obj.total_seconds()

    def field_change(self, field):
        # Calculate angle change
        time = self.time_diff(field)
        change = float(self.data[field]['data']) * time

        # Filter values close to 0 (avoid drift)
        # if ((abs(change) - 1) < 0):
        #   change = 0
        return change

    def gyr_change(self):
        change = {
            'x': self.field_change('gyr_x'),
            'y': self.field_change('gyr_y'),
            'z': self.field_change('gyr_z')
        }
        return change