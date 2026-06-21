# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28275():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    if str(data).startswith('https://admin.internal/'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
