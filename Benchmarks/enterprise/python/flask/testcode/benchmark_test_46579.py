# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest46579():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
