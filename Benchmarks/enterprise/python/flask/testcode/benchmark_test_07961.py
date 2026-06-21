# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07961():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    eval(str(data))
    return jsonify({"result": "success"})
