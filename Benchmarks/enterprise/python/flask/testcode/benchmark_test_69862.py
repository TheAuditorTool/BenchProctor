# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69862():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
