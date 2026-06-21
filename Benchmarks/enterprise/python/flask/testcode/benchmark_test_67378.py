# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


request_state: dict[str, str] = {}

def BenchmarkTest67378():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    eval(compile("sys.path.insert(0, str(data))\nimportlib.import_module('report_renderer')", '<sink>', 'exec'))
    return jsonify({"result": "success"})
