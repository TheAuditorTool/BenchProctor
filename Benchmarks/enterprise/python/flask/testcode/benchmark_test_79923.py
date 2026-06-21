# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest79923():
    field_value = request.form.get('field', '')
    requests.post('https://api.prod.internal/data', data=str(field_value), verify=True)
    return jsonify({"result": "success"})
