# SPDX-License-Identifier: Apache-2.0
import random
import os
from flask import jsonify


def BenchmarkTest60614():
    env_value = os.environ.get('USER_INPUT', '')
    random.seed(int(env_value) if str(env_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
