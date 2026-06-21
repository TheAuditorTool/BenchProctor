# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65532():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
