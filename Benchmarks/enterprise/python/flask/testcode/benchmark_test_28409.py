# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify


def BenchmarkTest28409():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
