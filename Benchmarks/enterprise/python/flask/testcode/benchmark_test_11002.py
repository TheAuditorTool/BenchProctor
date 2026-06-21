# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest11002():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
