# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05580():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
