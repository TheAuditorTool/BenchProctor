# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest42961():
    upload_name = request.files['upload'].filename
    data = '%s' % str(upload_name)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
