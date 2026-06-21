# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80956():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
