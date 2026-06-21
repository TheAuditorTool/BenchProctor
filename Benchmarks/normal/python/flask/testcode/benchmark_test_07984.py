# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest07984():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
