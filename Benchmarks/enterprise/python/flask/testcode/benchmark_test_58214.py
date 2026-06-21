# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58214():
    multipart_value = request.form.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
