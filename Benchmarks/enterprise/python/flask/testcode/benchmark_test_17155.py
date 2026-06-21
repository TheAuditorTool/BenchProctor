# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17155():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value}'
    exec(str(data))
    return jsonify({"result": "success"})
