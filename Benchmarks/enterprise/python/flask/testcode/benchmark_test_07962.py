# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07962():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
