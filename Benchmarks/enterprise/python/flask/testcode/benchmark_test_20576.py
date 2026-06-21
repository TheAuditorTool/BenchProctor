# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20576():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    int(str(data))
    return jsonify({"result": "success"})
