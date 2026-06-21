# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest62668():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
