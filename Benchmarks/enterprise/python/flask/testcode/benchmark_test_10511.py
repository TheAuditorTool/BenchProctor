# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10511():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return jsonify({'error': 'zero division'}), 400
    result = 100 / divisor
    return jsonify({"result": "success"})
