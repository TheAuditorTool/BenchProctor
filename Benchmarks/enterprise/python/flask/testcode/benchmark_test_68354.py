# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest68354():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
