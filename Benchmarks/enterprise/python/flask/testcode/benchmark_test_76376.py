# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76376():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
