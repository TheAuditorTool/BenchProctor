# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest08055():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    sys.path.insert(0, str(graphql_var))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
