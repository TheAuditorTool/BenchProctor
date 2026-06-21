# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest26559():
    multipart_value = request.form.get('multipart_field', '')
    data = ensure_str(multipart_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
