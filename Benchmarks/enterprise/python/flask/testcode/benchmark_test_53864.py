# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest53864():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
