# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def ensure_str(value):
    return str(value)

def BenchmarkTest06753():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ensure_str(header_value)
    def _primary():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
