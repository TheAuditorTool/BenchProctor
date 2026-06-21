# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22791():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return jsonify({'error': 'zero division'}), 400
    result = 100 / divisor
    return jsonify({"result": "success"})
