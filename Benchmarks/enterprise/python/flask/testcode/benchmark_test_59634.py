# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59634():
    raw_body = request.get_data(as_text=True)
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
