# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest05693(path_param):
    path_value = path_param
    data = default_blank(path_value)
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
