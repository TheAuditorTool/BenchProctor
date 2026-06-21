# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import pickle


def BenchmarkTest25947():
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
