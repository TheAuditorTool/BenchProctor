# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify


def BenchmarkTest77402():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
