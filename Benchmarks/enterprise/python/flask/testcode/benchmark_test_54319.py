# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54319():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
