# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26372():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
