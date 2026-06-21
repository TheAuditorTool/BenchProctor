# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest40183():
    host_value = request.headers.get('Host', '')
    kind = 'json' if str(host_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = host_value
            data = parsed
        case _:
            data = host_value
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
