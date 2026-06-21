# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest10446():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
