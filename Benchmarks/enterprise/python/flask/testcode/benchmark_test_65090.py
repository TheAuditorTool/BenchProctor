# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65090():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
