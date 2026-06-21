# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest54823():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
