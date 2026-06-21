# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72216():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    eval(str(data))
    return jsonify({"result": "success"})
