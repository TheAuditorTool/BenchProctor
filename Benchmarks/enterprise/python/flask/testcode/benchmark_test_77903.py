# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77903():
    referer_value = request.headers.get('Referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
