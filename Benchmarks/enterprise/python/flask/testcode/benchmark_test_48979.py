# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest48979():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
