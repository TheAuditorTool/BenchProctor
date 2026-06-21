# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43008():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    exec(str(data))
    return jsonify({"result": "success"})
