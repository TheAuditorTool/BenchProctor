# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66568():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
