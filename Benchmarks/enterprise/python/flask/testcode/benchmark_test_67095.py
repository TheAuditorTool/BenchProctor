# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest67095(path_param):
    path_value = path_param
    db.execute('SELECT * FROM users WHERE id = ' + str(path_value))
    return jsonify({"result": "success"})
