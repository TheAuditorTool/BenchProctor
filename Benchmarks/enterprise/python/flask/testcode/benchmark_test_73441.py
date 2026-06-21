# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest73441():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
