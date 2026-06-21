# SPDX-License-Identifier: Apache-2.0
import keyring
from flask import jsonify
from app_runtime import db


def BenchmarkTest00621():
    secret_value = 'default_setting_value'
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    store_cred = keyring.get_password('app', 'service-account')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return jsonify({"result": "success"})
