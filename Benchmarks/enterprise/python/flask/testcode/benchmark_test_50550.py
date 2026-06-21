# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50550():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
