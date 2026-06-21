# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55997():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
