# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import json


def BenchmarkTest11323():
    origin_value = request.headers.get('Origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
