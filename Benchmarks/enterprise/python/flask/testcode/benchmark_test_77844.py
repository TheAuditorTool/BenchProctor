# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77844():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
