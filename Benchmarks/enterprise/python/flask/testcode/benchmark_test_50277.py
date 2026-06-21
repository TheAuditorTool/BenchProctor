# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest50277():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
