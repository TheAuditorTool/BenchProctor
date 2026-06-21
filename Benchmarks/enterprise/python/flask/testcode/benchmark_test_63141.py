# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63141():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
