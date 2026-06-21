# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest01529():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
