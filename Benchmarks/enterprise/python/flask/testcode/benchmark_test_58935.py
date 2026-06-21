# SPDX-License-Identifier: Apache-2.0
import keyring
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest58935():
    secret_value = 'default_config_label'
    data, _sep, _rest = str(secret_value).partition('\x00')
    store_cred = keyring.get_password('app', 'service-account')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
