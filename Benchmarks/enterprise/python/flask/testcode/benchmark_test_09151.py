# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09151():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
