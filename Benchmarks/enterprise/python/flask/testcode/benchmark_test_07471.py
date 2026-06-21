# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07471():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
