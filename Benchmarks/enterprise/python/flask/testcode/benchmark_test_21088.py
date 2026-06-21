# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21088():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
