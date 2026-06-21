# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest30032():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
