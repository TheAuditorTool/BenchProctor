# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest77730():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    requests.get(str(data))
    return jsonify({"result": "success"})
