# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37954():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
