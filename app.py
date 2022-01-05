from flask import Flask
from flask import jsonify
from miio.integrations.vacuum.dreame.dreamevacuum_miot import DreameVacuumMiot
from decouple import config

app = Flask(__name__)

vacuumAddress = config('VACUUM_ADDRESS')
vacuumToken = config('VACUUM_TOKEN')

@app.route("/")
def index():
    vacuum = DreameVacuumMiot(vacuumAddress, vacuumToken)
    status = vacuum.status()
    return {
        "battery_level": status.battery_level,
        "device_status": status.device_status.name,
    }

@app.route('/start')
def start():
    vacuum = DreameVacuumMiot(vacuumAddress, vacuumToken)
    vacuum.start()
    return "Cleaning started"

@app.route('/pause')
def pause():
    vacuum = DreameVacuumMiot(vacuumAddress, vacuumToken)
    vacuum.stop()
    return "Cleaning paused"

@app.route('/home')
def home():
    vacuum = DreameVacuumMiot(vacuumAddress, vacuumToken)
    vacuum.home()
    return "Going home!"
