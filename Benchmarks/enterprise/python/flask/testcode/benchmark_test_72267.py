# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72267():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    return jsonify({'error': str(json_value), 'stack': repr(locals())}), 500
