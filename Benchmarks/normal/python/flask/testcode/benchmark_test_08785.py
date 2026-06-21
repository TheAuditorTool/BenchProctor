# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest08785():
    env_value = os.environ.get('USER_INPUT', '')
    os.chmod('/var/app/data/' + str(env_value), 0o777)
    return jsonify({"result": "success"})
