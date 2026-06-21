# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest76503():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
