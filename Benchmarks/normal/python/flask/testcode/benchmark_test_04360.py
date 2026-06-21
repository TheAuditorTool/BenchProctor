# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest04360():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data, _sep, _rest = str(secret_value).partition('\x00')
    db.connect(host='localhost', user='app', password=data)
    return jsonify({"result": "success"})
