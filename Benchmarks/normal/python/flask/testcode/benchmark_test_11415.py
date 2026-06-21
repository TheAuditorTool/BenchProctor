# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11415():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
