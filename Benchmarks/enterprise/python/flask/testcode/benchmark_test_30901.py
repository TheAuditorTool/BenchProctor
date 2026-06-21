# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30901():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
