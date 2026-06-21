# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import importlib


request_state: dict[str, str] = {}

def BenchmarkTest33520():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return jsonify({"result": "success"})
