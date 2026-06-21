# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest11842():
    secret_value = 'app_display_name'
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(secret_value), store_cred)
    return jsonify({"result": "success"})
