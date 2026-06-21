# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest48279():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
