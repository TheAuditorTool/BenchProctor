# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest48833():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    return jsonify({'error': 'An internal error occurred'}), 500
