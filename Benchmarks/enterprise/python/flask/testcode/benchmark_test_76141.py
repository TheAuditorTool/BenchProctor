# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest76141():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    os.seteuid(65534)
    return jsonify({"result": "success"})
