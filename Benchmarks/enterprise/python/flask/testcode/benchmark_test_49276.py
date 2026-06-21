# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest49276():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
