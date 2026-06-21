# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest48092():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
