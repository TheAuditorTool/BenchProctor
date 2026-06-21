# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import importlib


def BenchmarkTest09605():
    host_value = request.headers.get('Host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
