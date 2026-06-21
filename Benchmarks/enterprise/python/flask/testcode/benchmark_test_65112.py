# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import re
from flask import request, jsonify
import ast


def BenchmarkTest65112():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    processed = re.sub(r'\d+', '****', str(data))
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
