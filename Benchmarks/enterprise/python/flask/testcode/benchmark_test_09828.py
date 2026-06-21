# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest09828():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
