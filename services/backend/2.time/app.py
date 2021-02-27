import time
from config.config import *
from datetime import datetime


@app.route('/time', methods = ['GET'])
def export_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


