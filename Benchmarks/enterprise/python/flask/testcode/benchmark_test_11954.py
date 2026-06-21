# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11954():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
