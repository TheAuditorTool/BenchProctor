# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41618():
    referer_value = request.headers.get('Referer', '')
    data = '{}'.format(referer_value)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
