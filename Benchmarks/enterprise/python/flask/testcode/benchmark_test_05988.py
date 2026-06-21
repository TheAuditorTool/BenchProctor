# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05988():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
