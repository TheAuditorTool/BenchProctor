# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import json


def BenchmarkTest04715():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
