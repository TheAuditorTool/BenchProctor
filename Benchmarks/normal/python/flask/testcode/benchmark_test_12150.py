# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest12150(path_param):
    path_value = path_param
    data = normalise_input(path_value)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return jsonify({"result": "success"})
