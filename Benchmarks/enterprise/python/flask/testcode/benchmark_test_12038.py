# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12038():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
