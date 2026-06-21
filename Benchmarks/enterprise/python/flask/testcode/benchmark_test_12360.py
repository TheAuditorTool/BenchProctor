# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12360():
    referer_value = request.headers.get('Referer', '')
    values = str(referer_value).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
