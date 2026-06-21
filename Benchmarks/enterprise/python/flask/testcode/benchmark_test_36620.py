# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import ctypes


def to_text(value):
    return str(value).strip()

def BenchmarkTest36620():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
