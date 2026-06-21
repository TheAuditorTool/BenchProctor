# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest75282():
    secret_value = 'feature_flag_value'
    data = normalise_input(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
