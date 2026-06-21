# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest23586():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
