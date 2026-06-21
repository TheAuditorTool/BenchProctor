# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest75124():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = f'{secret_value:.200s}'
    db.connect(host='localhost', user='app', password=data)
    return jsonify({"result": "success"})
