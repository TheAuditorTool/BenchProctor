# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest05945():
    secret_value = 'default_setting_value'
    data = default_blank(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
