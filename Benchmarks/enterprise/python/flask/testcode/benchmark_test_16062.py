# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16062():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return jsonify({'error': 'zero division'}), 400
    result = 100 / divisor
    return jsonify({"result": "success"})
