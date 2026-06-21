# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest34329():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
