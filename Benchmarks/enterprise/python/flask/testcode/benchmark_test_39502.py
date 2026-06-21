# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest39502():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
