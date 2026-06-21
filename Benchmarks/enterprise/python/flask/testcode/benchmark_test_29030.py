# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest29030():
    upload_name = request.files['upload'].filename
    requests.post('https://api.prod.internal/data', data=str(upload_name), verify=True)
    return jsonify({"result": "success"})
