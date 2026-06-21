# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest36565():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
