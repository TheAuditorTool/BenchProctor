# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
import ast


def BenchmarkTest40215():
    xml_value = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
