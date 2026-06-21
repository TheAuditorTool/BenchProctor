# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27487():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
