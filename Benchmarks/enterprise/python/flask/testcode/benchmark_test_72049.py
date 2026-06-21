# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import re
from flask import jsonify
import ast


def BenchmarkTest72049(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(processed))
    return resp
