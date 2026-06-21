# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest05068():
    referer_value = request.headers.get('Referer', '')
    data = relay_value(referer_value)
    processed = data[:64]
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(processed)}
