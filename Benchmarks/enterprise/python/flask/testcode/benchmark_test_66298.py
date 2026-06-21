# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest66298():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
