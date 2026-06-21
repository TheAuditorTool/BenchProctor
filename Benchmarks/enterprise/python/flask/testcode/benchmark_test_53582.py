# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53582():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
