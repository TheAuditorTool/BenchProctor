# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13229():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
