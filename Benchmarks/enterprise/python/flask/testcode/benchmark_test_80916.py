# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest80916():
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
