# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest62233():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    int(str(data))
    return jsonify({"result": "success"})
