# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest22859():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    os.seteuid(65534)
    return jsonify({"result": "success"})
