# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest24131():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
