# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29108():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
