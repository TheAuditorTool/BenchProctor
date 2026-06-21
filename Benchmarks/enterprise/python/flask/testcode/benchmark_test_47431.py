# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest47431():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
