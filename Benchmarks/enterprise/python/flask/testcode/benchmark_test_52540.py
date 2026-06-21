# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest52540():
    field_value = request.form.get('field', '')
    data = relay_value(field_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
