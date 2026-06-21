# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest21338():
    secret_value = 'default_setting_value'
    data = to_text(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
