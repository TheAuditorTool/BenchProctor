# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest76054():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
