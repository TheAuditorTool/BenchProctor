# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest80955():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = '{}'.format(yaml_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
