# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest04873():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
