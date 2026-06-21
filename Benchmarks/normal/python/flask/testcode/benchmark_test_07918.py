# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time


def relay_value(value):
    return value

def BenchmarkTest07918():
    upload_name = request.files['upload'].filename
    data = relay_value(upload_name)
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})
