# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest01382():
    field_value = request.form.get('field', '')
    data = to_text(field_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
