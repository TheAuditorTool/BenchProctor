# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest13280():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return jsonify({"result": "success"})
