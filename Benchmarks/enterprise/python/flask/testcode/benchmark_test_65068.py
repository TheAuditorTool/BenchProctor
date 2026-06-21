# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest65068():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
