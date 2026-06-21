# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import pickle


def BenchmarkTest24719():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return jsonify({"result": "success"})
