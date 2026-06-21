# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest25169():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
