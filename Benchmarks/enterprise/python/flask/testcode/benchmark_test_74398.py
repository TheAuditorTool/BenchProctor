# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest74398():
    env_value = os.environ.get('USER_INPUT', '')
    trusted_claim = str(env_value)
    return jsonify({'trusted': trusted_claim}), 200
