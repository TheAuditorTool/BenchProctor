# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69916():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
