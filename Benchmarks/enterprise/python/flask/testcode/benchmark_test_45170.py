# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest45170():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
