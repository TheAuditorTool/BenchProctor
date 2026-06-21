# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17131():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
