# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest01862():
    secret_value = 'default_setting_value'
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    store_cred = os.environ.get('APP_SECRET', '')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return jsonify({"result": "success"})
