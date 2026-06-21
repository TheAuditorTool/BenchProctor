# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40159():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
