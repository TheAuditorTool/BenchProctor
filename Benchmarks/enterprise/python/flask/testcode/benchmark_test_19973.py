# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest19973():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
