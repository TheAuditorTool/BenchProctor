# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest45088():
    secret_value = 'config_secret_test_abc123'
    data = relay_value(secret_value)
    db.connect(host='localhost', user='app', password=data)
    return jsonify({"result": "success"})
