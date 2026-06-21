# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import ast


def BenchmarkTest75039():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
