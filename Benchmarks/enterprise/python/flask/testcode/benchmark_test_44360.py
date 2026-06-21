# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44360():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body}'
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return jsonify({'error': 'zero division'}), 400
    result = 100 / divisor
    return jsonify({"result": "success"})
