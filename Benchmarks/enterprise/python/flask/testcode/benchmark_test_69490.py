# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69490():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % (forwarded_ip,)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
