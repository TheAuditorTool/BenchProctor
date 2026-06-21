# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest68699():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
