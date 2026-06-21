# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify


def BenchmarkTest48022():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
