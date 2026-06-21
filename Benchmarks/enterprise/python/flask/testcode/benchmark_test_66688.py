# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66688():
    referer_value = request.headers.get('Referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
