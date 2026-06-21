# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import importlib
import sys


def BenchmarkTest09414():
    host_value = request.headers.get('Host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
