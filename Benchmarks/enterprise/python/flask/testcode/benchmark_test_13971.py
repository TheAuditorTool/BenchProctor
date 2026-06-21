# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest13971():
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
