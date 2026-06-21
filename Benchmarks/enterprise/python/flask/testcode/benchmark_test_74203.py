# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest74203():
    secret_value = 'feature_flag_value'
    prefix = ''
    data = prefix + str(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return jsonify({"result": "success"})
