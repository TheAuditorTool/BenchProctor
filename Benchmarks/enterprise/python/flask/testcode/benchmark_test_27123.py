# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27123():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
