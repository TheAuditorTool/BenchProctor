# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55379():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
