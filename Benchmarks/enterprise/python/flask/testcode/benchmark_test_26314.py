# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify


def BenchmarkTest26314():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
