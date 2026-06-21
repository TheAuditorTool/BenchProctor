# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest17731():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    int(str(data))
    return jsonify({"result": "success"})
