# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05881():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
