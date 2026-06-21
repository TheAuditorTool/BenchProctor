# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47139():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
