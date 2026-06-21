# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43864():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
