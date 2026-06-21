# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42446():
    referer_value = request.headers.get('Referer', '')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(referer_value)}
