# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest50986(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
