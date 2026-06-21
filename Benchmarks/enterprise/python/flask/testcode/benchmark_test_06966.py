# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest06966():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
