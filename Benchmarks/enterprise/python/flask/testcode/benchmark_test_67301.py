# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67301():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
