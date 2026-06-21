# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify


def BenchmarkTest40166():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
