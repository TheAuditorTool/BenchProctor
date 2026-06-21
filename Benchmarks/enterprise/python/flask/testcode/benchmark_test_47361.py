# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest47361():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
