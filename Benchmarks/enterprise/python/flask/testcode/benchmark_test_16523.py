# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest16523():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
