# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify


def BenchmarkTest08654():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
