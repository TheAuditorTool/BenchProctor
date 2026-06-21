# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest30040():
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
