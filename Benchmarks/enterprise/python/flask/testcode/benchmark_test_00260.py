# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest00260():
    field_value = request.form.get('field', '')
    _resp = requests.get(str(field_value))
    exec(_resp.text)
    return jsonify({"result": "success"})
