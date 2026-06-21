# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59629():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
