# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest75713():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
