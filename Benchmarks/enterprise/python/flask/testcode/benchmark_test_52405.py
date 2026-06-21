# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52405():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
