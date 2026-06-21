# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07291():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
