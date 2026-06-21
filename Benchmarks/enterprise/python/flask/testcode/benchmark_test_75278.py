# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest75278():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
