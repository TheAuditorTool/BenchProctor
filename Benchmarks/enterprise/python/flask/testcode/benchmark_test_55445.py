# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55445():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
