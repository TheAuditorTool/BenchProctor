# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest06206():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
