# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02891():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
