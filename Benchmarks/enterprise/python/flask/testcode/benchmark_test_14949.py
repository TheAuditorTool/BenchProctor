# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14949():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
