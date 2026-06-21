# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest05362():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
