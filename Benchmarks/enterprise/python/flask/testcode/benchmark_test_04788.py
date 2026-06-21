# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest04788():
    env_value = os.environ.get('USER_INPUT', '')
    match str(env_value):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
