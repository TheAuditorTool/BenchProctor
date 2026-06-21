# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest63442():
    raw_body = request.get_data(as_text=True)
    data = relay_value(raw_body)
    processed = data[:64]
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(processed)}
