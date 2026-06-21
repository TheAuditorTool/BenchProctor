# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


request_state: dict[str, str] = {}

def BenchmarkTest17561():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    def _primary():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
