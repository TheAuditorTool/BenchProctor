# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74819():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
