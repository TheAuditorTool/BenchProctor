# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest22278():
    secret_value = 'default_config_label'
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(secret_value), store_cred)
    return jsonify({"result": "success"})
