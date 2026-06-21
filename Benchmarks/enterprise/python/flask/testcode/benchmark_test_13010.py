# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest13010():
    env_value = os.environ.get('USER_INPUT', '')
    match str(env_value):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
