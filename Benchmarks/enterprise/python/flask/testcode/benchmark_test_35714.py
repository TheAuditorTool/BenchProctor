# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35714():
    origin_value = request.headers.get('Origin', '')
    data = str(origin_value).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
