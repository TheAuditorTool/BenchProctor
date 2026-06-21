# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48890():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
