# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest33396():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = str(secret_value).replace('\x00', '')
    db.connect(host='localhost', user='app', password=data)
    return jsonify({"result": "success"})
