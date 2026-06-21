# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest27765():
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
