# SPDX-License-Identifier: Apache-2.0
import random
import os
from flask import jsonify


def BenchmarkTest52784():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
