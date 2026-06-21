# SPDX-License-Identifier: Apache-2.0
import random
import os
from flask import jsonify


def BenchmarkTest04857():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
