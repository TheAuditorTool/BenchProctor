# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02285():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
