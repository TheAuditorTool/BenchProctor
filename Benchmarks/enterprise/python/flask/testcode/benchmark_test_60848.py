# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60848():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
