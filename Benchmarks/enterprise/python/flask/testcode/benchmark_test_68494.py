# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest68494():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
