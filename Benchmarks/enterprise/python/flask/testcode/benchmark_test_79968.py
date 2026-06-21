# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest79968():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
