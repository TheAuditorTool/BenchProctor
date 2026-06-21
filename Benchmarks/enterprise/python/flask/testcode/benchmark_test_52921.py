# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52921():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
