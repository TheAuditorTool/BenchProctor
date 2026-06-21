# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest53288():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
