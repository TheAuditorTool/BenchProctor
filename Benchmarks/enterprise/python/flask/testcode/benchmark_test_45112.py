# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import json


def BenchmarkTest45112():
    host_value = request.headers.get('Host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
