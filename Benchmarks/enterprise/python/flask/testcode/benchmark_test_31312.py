# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest31312():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(config_value), store_cred)
    return jsonify({"result": "success"})
