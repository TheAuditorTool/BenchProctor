# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest66184():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
