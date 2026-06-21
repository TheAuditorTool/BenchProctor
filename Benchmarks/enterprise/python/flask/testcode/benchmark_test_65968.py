# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65968():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
