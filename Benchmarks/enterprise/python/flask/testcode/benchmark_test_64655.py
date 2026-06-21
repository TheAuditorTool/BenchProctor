# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest64655():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = '{}'.format(secret_value)
    db.connect(host='localhost', user='app', password=data)
    return jsonify({"result": "success"})
