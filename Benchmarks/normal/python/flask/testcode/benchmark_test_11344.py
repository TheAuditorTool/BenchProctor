# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest11344():
    field_value = request.form.get('field', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(field_value)}, verify=True)
    return jsonify({"result": "success"})
