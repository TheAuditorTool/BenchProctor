# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import ast


def BenchmarkTest76559():
    referer_value = request.headers.get('Referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    json.loads(data)
    return jsonify({"result": "success"})
