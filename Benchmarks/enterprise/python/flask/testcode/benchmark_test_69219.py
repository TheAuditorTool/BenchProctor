# SPDX-License-Identifier: Apache-2.0
import keyring
from flask import jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest69219():
    secret_value = 'default_config_label'
    data = ensure_str(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return jsonify({"result": "success"})
