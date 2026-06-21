# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70362():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    prefix = ''
    data = prefix + str(json_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
