# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest26392():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = f'{secret_value}'
    db.connect(host='localhost', user='app', password=data)
    return jsonify({"result": "success"})
