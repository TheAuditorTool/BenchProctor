# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest25958(path_param):
    path_value = path_param
    data = to_text(path_value)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return jsonify({"result": "success"})
