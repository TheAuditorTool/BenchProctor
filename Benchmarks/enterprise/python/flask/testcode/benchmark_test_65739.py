# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest65739():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    return jsonify({'error': 'An internal error occurred'}), 500
