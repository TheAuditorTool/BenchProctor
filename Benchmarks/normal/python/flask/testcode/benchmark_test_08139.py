# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest08139():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = str(secret_value).replace('\x00', '')
    db.connect(host='localhost', user='app', password=data)
    return jsonify({"result": "success"})
