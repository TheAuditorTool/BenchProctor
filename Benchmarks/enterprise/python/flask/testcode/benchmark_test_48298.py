# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48298():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
