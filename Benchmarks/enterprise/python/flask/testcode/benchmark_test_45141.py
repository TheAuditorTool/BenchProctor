# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45141():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = ' '.join(str(json_value).split())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
