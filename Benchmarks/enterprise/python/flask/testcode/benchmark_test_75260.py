# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75260():
    referer_value = request.headers.get('Referer', '')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(referer_value)}
