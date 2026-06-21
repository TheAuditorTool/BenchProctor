# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest09740():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(config_value)
    data = collected
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
