# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00812():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
