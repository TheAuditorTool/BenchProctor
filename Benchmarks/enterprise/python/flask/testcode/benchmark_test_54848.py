# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest54848():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    session['data'] = str(graphql_var)
    return jsonify({"result": "success"})
