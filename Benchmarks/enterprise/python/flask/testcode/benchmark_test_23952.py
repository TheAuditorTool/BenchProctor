# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23952():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    if str(data).startswith('https://admin.internal/'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
