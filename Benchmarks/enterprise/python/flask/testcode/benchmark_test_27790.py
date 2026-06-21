# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest27790():
    secret_value = 'default_config_label'
    data = relay_value(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
