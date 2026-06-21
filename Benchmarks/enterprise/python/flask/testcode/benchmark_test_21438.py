# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest21438():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
