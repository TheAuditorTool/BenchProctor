# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest00325():
    env_value = os.environ.get('USER_INPUT', '')
    base_name = os.path.basename(str(env_value))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})
