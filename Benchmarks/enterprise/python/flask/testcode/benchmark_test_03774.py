# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest03774():
    host_value = request.headers.get('Host', '')
    data = normalise_input(host_value)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
