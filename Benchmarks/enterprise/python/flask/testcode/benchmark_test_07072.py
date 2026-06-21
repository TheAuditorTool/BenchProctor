# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07072():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
