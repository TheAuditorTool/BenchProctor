# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest08783():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return str(processed), 200, {'Content-Type': 'text/html'}
