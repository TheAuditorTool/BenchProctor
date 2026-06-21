# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50617():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = str(json_value).replace('\x00', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
