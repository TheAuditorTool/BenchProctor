# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest47097():
    upload_name = request.files['upload'].filename
    data = ensure_str(upload_name)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
