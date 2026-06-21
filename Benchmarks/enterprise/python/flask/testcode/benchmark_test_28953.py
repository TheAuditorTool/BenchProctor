# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify


def BenchmarkTest28953():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
