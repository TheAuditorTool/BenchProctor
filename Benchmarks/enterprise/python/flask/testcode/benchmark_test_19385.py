# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19385():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    if str(data).startswith('https://admin.internal/'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
