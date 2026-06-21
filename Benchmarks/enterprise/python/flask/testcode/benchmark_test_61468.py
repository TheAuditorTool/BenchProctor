# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61468():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
