# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest08977():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
