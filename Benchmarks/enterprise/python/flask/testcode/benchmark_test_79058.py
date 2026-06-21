# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest79058():
    host_value = request.headers.get('Host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
