# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify


def BenchmarkTest65307():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
