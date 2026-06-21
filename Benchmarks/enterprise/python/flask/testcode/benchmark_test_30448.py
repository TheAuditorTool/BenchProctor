# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest30448():
    upload_name = request.files['upload'].filename
    data = relay_value(upload_name)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
