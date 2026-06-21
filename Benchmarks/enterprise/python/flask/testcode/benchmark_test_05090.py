# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest05090():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    prefix = ''
    data = prefix + str(config_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
