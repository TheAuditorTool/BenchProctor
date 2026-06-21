# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest08049():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data, _sep, _rest = str(secret_value).partition('\x00')
    db.connect(host='localhost', user='app', password=data)
    return jsonify({"result": "success"})
