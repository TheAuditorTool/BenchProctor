# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20520():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
