# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import re


def relay_value(value):
    return value

def BenchmarkTest12850():
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
