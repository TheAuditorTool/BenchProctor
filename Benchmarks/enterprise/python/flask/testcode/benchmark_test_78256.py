# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78256():
    origin_value = request.headers.get('Origin', '')
    return jsonify({'error': str(origin_value), 'stack': repr(locals())}), 500
