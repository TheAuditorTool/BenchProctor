# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72035():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    eval(str(data))
    return jsonify({"result": "success"})
