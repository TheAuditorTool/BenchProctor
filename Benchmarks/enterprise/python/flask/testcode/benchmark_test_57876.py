# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57876():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
