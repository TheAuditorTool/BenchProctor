# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest18324():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
