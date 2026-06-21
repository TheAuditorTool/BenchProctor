# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest63350():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
