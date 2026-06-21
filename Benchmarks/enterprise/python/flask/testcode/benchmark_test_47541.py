# SPDX-License-Identifier: Apache-2.0
from flask import session
import json
from flask import request, jsonify


def BenchmarkTest47541():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    session['data'] = str(data)
    return jsonify({"result": "success"})
