# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest77418():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
