# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest44483():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
