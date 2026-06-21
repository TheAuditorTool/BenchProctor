# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56680():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
