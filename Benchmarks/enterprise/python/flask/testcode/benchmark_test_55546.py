# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55546():
    host_value = request.headers.get('Host', '')
    return jsonify({'error': str(host_value), 'stack': repr(locals())}), 500
