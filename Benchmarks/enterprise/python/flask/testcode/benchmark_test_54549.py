# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest54549():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
