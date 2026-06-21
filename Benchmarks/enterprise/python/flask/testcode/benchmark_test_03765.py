# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify
import ast


def BenchmarkTest03765():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.chmod('/var/app/data/' + str(processed), 0o777)
    return jsonify({"result": "success"})
