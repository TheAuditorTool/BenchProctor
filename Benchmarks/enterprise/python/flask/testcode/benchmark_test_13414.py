# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest13414():
    env_value = os.environ.get('USER_INPUT', '')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(env_value)}
