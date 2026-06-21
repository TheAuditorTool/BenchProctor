# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest13133():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
