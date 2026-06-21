# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify
import ast


def BenchmarkTest10981():
    referer_value = request.headers.get('Referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    yaml.safe_load(data)
    return jsonify({"result": "success"})
