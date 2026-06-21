# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11710():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
