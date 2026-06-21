# SPDX-License-Identifier: Apache-2.0
import keyring
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest57645():
    secret_value = 'feature_flag_value'
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    store_cred = keyring.get_password('app', 'service-account')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
