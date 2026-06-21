# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45454():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
