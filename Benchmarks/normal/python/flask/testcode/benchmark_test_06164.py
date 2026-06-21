# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify


def BenchmarkTest06164():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
