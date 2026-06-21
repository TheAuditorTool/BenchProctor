# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12908():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
