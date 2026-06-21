# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04344():
    raw_body = request.get_data(as_text=True)
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
