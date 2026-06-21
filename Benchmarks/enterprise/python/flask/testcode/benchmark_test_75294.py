# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75294():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body}'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
