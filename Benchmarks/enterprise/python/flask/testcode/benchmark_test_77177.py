# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest77177():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
