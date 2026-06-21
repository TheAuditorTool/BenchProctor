# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50893():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
