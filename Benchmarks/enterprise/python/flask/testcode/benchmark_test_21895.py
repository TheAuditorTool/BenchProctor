# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21895():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
