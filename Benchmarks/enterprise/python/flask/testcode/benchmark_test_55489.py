# SPDX-License-Identifier: Apache-2.0
import random
import os
from flask import jsonify


def BenchmarkTest55489():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
