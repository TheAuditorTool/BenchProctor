# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33456():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value}'
    int(str(data))
    return jsonify({"result": "success"})
