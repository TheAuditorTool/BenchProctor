# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42819():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
