# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest19813():
    field_value = request.form.get('field', '')
    requests.post('http://api.prod.internal/data', data=str(field_value))
    return jsonify({"result": "success"})
