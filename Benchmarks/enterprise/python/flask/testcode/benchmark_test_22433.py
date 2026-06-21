# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22433():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
