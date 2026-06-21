# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest38679():
    env_value = os.environ.get('USER_INPUT', '')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(env_value))
    return jsonify({'lookup': arr[idx]}), 200
