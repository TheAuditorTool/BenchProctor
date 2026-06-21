# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59357():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
