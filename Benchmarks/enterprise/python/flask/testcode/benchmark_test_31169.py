# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31169():
    auth_header = request.headers.get('Authorization', '')
    data = '{}'.format(auth_header)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
