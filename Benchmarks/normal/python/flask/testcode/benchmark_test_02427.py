# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02427():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
