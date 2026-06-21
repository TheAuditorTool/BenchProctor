# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00919():
    origin_value = request.headers.get('Origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    int(str(data))
    return jsonify({"result": "success"})
