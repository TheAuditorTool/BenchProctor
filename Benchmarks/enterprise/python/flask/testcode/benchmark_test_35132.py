# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35132():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
