# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest69763():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})
