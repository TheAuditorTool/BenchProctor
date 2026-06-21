# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest44929():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
