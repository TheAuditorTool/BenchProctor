# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest22446():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
