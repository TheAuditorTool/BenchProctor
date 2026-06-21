# SPDX-License-Identifier: Apache-2.0
import keyring
from flask import jsonify
from app_runtime import db


def BenchmarkTest80675():
    secret_value = 'default_config_label'
    data = secret_value if secret_value else 'default'
    store_cred = keyring.get_password('app', 'service-account')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return jsonify({"result": "success"})
