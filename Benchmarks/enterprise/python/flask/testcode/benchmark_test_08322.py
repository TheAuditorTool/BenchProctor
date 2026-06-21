# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest08322():
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
