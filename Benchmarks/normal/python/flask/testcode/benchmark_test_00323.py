# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00323():
    origin_value = request.headers.get('Origin', '')
    processed = 'true' if str(origin_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
