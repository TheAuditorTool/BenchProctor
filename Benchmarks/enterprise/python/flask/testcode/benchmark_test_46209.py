# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46209():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
