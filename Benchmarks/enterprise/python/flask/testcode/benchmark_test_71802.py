# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71802():
    origin_value = request.headers.get('Origin', '')
    return jsonify({'error': str(origin_value), 'stack': repr(locals())}), 500
