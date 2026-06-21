# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest07414():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
