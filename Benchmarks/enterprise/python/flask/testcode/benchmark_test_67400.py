# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67400():
    origin_value = request.headers.get('Origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
