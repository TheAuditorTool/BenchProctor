# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60581():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
