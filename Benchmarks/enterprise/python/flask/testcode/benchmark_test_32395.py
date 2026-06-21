# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32395():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
